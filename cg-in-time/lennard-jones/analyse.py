#!/bin/python3
""" Analysis of a LAMMPS simulation

When running this script then it computes

1. Summary of thermodynamic data.
2. The time correlation function of the potential energy.
3. The mean squared displacement (MSD) of the particles, and the diffusion coefficient.

"""

import numpy as np

def read_dump(filename='dump.lammps', verbose=False):
    c = 0
    box=[[0, 10],[0, 10],[0, 10]]
    with open(filename) as file:
        line = file.readline()
        frames=[]
        while line:
            c = c + 1
            if 'ITEM: NUMBER OF ATOMS' in line:
                line = file.readline()
                number_of_atoms = int(line)
                types = np.zeros(number_of_atoms, dtype=int)
                if verbose:
                    print(f'{number_of_atoms=}')
            if 'ITEM: BOX BOUNDS' in line:
                for dim in 0, 1, 2:
                    elms = file.readline().split()
                    box[dim] = [float(elms[0]), float(elms[1])]
                if verbose:
                    print(f'{box=}')
            if 'ITEM: ATOMS' in line:
                pos = np.zeros((number_of_atoms, 3), dtype=float)
                elms = line.split()
                columns = elms[2:]
                if verbose:
                    print(f'{columns=}')
                def find(c, s):
                    for i, e in enumerate(c):
                        if s in e:
                            return i
                idx_id = find(columns, 'id')
                idx_type = find(columns, 'type')
                idx_xs = find(columns, 'xs')
                idx_ys = find(columns, 'ys')
                idx_zs = find(columns, 'zs')
                idx_ix = find(columns, 'ix')
                idx_iy = find(columns, 'iy')
                idx_iz = find(columns, 'iz')                
                for _ in range(number_of_atoms):
                    elms = file.readline().split()
                    i = int(elms[idx_id])-1  # Note: LAMMPS start counting at zero
                    t = int(elms[idx_type])
                    x = (float(elms[idx_xs])+float(elms[idx_ix]))
                    x = x*(box[0][1]-box[0][0])
                    y = (float(elms[idx_ys])+float(elms[idx_iy]))
                    y = y*(box[1][1]-box[1][0])
                    z = (float(elms[idx_zs])+float(elms[idx_iz]))
                    z = z*(box[0][1]-box[0][0])
                    types[i] = t
                    pos[i, 0] = x
                    pos[i, 1] = y
                    pos[i, 2] = z
                frames.append(pos)
            line = file.readline()
    return np.array(frames), np.array(box), types

def remove_drift(frames):
    """ Remove drift of geometric_center"""
    geometric_center = frames.mean(axis=1)
    return frames - geometric_center[:,np.newaxis,:]

def compute_mean_squared_displacement(frames, f_i = 0):
    frames = remove_drift(frames)
    MSD = ((frames[f_i, :]-frames)**2).mean(axis=1).mean(axis=1)
    return MSD

def thermo_data_as_dataframe(filename='log.lammps', time_step=None, first_frame=0, stride_frame=1, last_frame=None):
    ''' Read thermodynamic data from LAMMPS log file '''
    import pandas as pd
    with open(filename) as file:
        not_found_beginning = True
        while not_found_beginning:
            elements = file.readline().split()
            if len(elements) > 0:
                if elements[0] == 'Step':
                    not_found_beginning = False
        columns = elements
        elements = file.readline().split()
        data = []
        frame = 0
        while len(elements) == len(columns):
            frame = frame + 1
            if frame > first_frame and (frame-1)%stride_frame==0:
                data.append([float(x) for x in elements])
            if last_frame and frame > last_frame:
                break
            elements = file.readline().split()
    dataframe = pd.DataFrame(columns=columns, data=data)
    if time_step:
        dataframe.insert(loc=0, column='Time', value=dataframe['Step'] * time_step)
    return dataframe


def run_avg(x, n=128):
    '''  Running average of n data points. '''
    from numpy import mean, zeros
    N = int(len(x) / n)
    out = zeros(N)
    for i in range(N):
        start = i * n
        stop = (i + 1) * n
        out[i] = mean(x[start:stop])
    return out


def run_avg_log(x, points_per_decade=24, base=None):
    """ Logarithmic averaging."""
    from numpy import mean, array
    if not base:
        base = 10 ** (1 / points_per_decade)
    if base < 1:
        print('Warning: Base should be larger than 1')
    floor, ceil, next_ceil = 0, 1, 1.0
    out = []
    while ceil < x.size:
        out.append(mean(x[floor:ceil]))
        # Set limits for next average range
        floor = ceil
        while int(next_ceil) == ceil:
            next_ceil = next_ceil * base
        ceil = int(next_ceil)
    return array(out)


def time_correlation(x, y=None):
    r''' Compute the time correlation function 
    The time correlation function :math:`C(t)` is computed using
    the Wienerâ€“Khinchin theorem with the FFT algorithm and zero padding.

     .. math::

         C(t) = \langle \Delta x(\tau) \Delta y(\tau + t) \rangle_\tau

         \Delta x(t) = x(t) - \langle x \rangle

         \Delta y(t) = x(y) - \langle y \rangle

    '''
    from numpy import conj, mean, real
    from numpy.fft import fft, ifft
    if y is None:
        y = x
    n = x.size
    fx = fft(x - mean(x), n=2 * n)
    fy = fft(y - mean(y), n=2 * n)
    fxy = conj(fx) * fy / n
    xy = ifft(fxy)[:n]
    return real(xy)


def frequency_dependent_response(x, y=None, dt=1.0, prefactor=1.0):
    r''' Frequency dependent responce
    The frequency dependent responce :math:`\mu(\omega)` is estimate from time-series
    assuming the fluctuation-dissipation theorem.

     .. math::

         \mu(\omega) = A\int_0^\infty \dot C(t)\exp(-i \omega t) dt

         \dot C(t) = \frac{d}{dt} \langle \Delta x(\tau) \Delta y(\tau + t) \rangle_\tau

         \Delta x(t) = x(t) - \langle x \rangle

         \Delta y(t) = y(t) - \langle y \rangle

    dt is the sample time of the time-series.
    Notice that the user must provide a prefactor
    to get the correct scaling responce function.
    The prefactor (:math:`A`) is -1/kT**2
    for the frequency dependent heat capacity.
    If y is None then it is set to be the same as the x time-series.
    The implimentation uses the FFT algorithm
    with zero-padding for Laplace transform,
    thus the calculation scales as $N\ln(N)$.

    Returns::

        omega, mu

     '''
    from numpy import arange, pi
    n = x.size
    k = arange(0, n)  # k = 0, 1, ... , n-1
    omega = 2 * pi * k / dt / n

    from numpy.fft import fft
    from numpy import gradient
    if y is None:
        y = x
    C = gradient(time_correlation(x, y))
    mu = prefactor * fft(C, n=2 * n)[:n]
    return omega, mu


def main():
    import matplotlib.pyplot as plt
    import time
    import numpy as np
    import pandas as pd

    # Load data
    tic = time.perf_counter()
    first_frame = 0
    frame_stride = 1    
    last_frame = None
    time_step = 2e-15
    steps_per_printout = 40
    print(f'{first_frame = } {frame_stride = } {last_frame = } {steps_per_printout = }')
    spns = int(1e-9 / time_step / steps_per_printout / frame_stride)  # Steps per nanosecond
    print(f'Steps per nanosecond: {spns = }')
    df = thermo_data_as_dataframe(filename='log.lammps',
                                  time_step=time_step,
                                  first_frame=first_frame,
                                  stride_frame=frame_stride,
                                  last_frame=last_frame)
    toc = time.perf_counter()
    print(f'Wallclock time to load data: {toc-tic} s')

    print(df.head())
    print(df.tail())
    print(f'Trajectory of {df.Time.max()/1e-9} ns')
    
    for column in df:
        print(f'Mean {column}: {df[column].mean() }')
    
    # Plot pressure
    plt.figure()
    # plt.plot(df.Time, df.Press, color='gray')
    n = spns
    plt.plot(run_avg(df.Time * 1e9, n), run_avg(df.Press, n), 'bo')
    plt.title(f'{df.Press.mean()=}')
    plt.ylabel('Pressure [atm]')
    plt.xlabel('Time [ns]')
    plt.savefig('Press.png', dpi=72, bbox_inches='tight')
    plt.show()

    # Thermodynamic summary
    df.describe().to_csv('thermo_stats.csv')
    print(f'{df.Temp.mean() = }\n'
          f'{df.Density.mean() = }\n'
          f'{df.Press.mean() = }\n'
          f'{df.PotEng.mean() = }\n'
          , file=open('thermo_stats.txt', 'w'))

    N = len(df)
    Nl2 = 2**int(np.log2(N))
    print(f"{N} is near {Nl2} = 2**{int(np.log2(Nl2))} ")
    
    # Energy time correlation
    plt.figure()
    tic = time.perf_counter()
    xx = df.Time[:Nl2]
    yy = df.PotEng[-Nl2:]
    c = time_correlation(yy) / yy.var()
    toc = time.perf_counter()
    print(f'Wallclock time for FFT: {toc-tic} s')
    x, y = run_avg_log(xx * 1e9), run_avg_log(c)
    plt.plot(x, y)
    plt.xlabel(r'Time, $t$ [ns]')
    plt.ylabel(r'$\langle \Delta U(0) \Delta U(t) \rangle/\langle (\Delta U)^2 \rangle$')
    plt.ylim(-0.02, 0.1)
    plt.xscale('log')
    plt.savefig('energy_correlation.png', dpi=72, bbox_inches='tight')
    plt.show()
    
    pd.DataFrame({
        'Time': x,
        'C_EE': y
    }).to_csv('time_correlation.csv', index=False)

    # Mean squared displacement
    tic = time.perf_counter()
    frames, box, types = read_dump('dump.constant_volume')
    toc = time.perf_counter()
    print(f'Wall clock time to read positions: {toc-tic} s')
    tic = time.perf_counter()
    MSD = compute_mean_squared_displacement(frames)
    toc = time.perf_counter()
    print(f'Wall clock time to compute MSD: {toc-tic} s')
    t = 50000*2e-15*1e9*np.arange(len(MSD))
    ii = int(len(MSD)/2)
    D = np.mean(MSD[:ii])/np.mean(t[:ii])/6
    print(f'{D= }')
    print(f'{D= }', file=open('info.txt', 'a'))    
    plt.figure()
    plt.title(f'{D= }')
    plt.plot(t, MSD, 'o-')
    plt.plot(t, 6*D*t, '--')
    plt.xlabel(r'Time, $t$ [ns]')
    plt.ylabel(r'Mean Squared Displacement [Ã…$^2$]')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('mean_squared_displacement.png', dpi=72, bbox_inches='tight')
    plt.show()

    pd.DataFrame({
        'Time': t,
        'MSD': MSD
    }).to_csv('mean_squared_displacement.csv', index=False)


if __name__ == '__main__':
    main()
