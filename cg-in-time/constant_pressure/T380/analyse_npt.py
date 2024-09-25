"""
Heat capacity and thermodynamic properties of o-terphenyl crystal, glass and liquid,
J. Chem. D Phys., 1972, 56, 503-516

"""

import os

import matplotlib.pyplot as plt
import numpy as np

current_directory = os.path.dirname(os.path.realpath(__file__))
print(f'Current directory: {current_directory}')

def thermo_data_as_dataframe(filename='log.lammps', time_step=None,
                             first_frame=0, stride_frame=1, last_frame=None, verbose=False):
    """ Read thermodynamic data from LAMMPS log file """
    import pandas as pd
    if verbose:
        print(f'Reading data from {filename}')
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
            if verbose and frame % 100_000 == 0:
                print(f'Frame {frame}')
            if frame > first_frame and (frame-1)%stride_frame==0:
                data.append([float(x) for x in elements])
            if last_frame and frame > last_frame:
                break
            elements = file.readline().split()
    dataframe = pd.DataFrame(columns=columns, data=data)
    if time_step:
        dataframe.insert(loc=0, column='Time', value=dataframe['Step'] * time_step)
    return dataframe

# Load data
time_step = 2e-15  # s
print(f'Time step: {time_step} s')
first_frame = 2**21
df = thermo_data_as_dataframe(filename='../../../log-file/constant_pressure/log.otp', time_step=time_step, first_frame=first_frame, verbose=True)
print(f'Columns: {df.columns}')
print(f'Number of frames: {len(df)}')

print(f'Time of first frame: {df["Time"].iloc[0]} s')
print(f'Time of last frame: {df["Time"].iloc[-1]} s')
print(f'Elapsed time: {df["Time"].iloc[-1] - df["Time"].iloc[0]} s')

# Constants
print('..:: Constants ::..')
pressure_to_SI = 101325  # atm to Pa
kcal_to_joules = 4184  # kcal/mol to J/mol
N_A = 6.02214076e23  # Avogadro's number
energy_to_SI = kcal_to_joules / N_A  # kcal/mol to J/unit
volume_to_SI = 1e-30  # Angstrom^3 to m^3
k_B = 1.38064852e-23  # J/K
print(f'k_B:         {k_B:6.2e} J/K')
number_of_molecules = 125
print(f'Number of molecules: {number_of_molecules}')
molar_mass = 230.3038 # g/mol
print(f'Molar mass: {molar_mass} g/mol')


# Average values
print('..:: Average values ::..')
temperature = df['Temp'].mean()
print(f'Temperature: {temperature:6.0f} K')
pressure = df['Press'].mean()
print(f'Pressure:    {pressure:6.2f} atm')
pressure_SI = pressure * pressure_to_SI
print(f'Pressure:    {pressure_SI:6.0f} Pa')
potential_energy = df['PotEng'].mean()
print(f'Pot. energy: {potential_energy:6.0f} Kcal/mole')
potential_energy_SI = potential_energy * energy_to_SI
print(f'Pot. energy: {potential_energy_SI:6.2e} J/unit')
volume = df['Volume'].mean()
print(f'Volume:      {volume:6.0f} Å^3')
volume_SI = volume * volume_to_SI
print(f'Volume:      {volume_SI:6.2e} m^3')
volume_molar = volume_SI * N_A / number_of_molecules
print(f'Volume:      {volume_molar:6.2e} m^3/mol')
print(f'Volume:      {volume_molar*1e6:6.2f} cm^3/mol')


# Compute isobaric heat capacity from enthalpy fluctuations
#  C_P = ( <H^2> - <H>^2 ) / ( k_B * T^2 )
enthalpy = (df['PotEng'] + df['KinEng'])*energy_to_SI + pressure_SI * df['Volume'] * volume_to_SI
# Equation 2.93 in Allen and Tildesley
c_p = enthalpy.var() / (k_B * temperature**2) / number_of_molecules
print(f'c_P (SI):         {c_p:6.2e} J/K/atom')
c_p_molar = c_p * N_A
print(f'c_P:         {c_p_molar:6.2f} J/mol/K')
print(f'c_P:         {c_p*N_A/molar_mass:6.2f} J/g/K')

# Compute isothermal compressibility from volume fluctuations
#  kappa_T = ( <V^2> - <V>^2 ) / ( k_B * T * <V>)
# Equation 2.93 in Allen and Tildesley
kappa_T = (df['Volume']*volume_to_SI).var() / (k_B * temperature * volume*volume_to_SI)
print(f'kappa_T:     {kappa_T:6.2e} Pa^-1')
bulk_modulus = 1/kappa_T
print(f'Bulk modulus:{bulk_modulus/1e9:6.2f} GPa')

# Compute isobaric expansion coefficient from volume and enthalpy fluctuations
#  alpha = cov(V, H) / ( k_B * T^2 * V )
# Equation 2.94 in Allen and Tildesley
alpha_p = np.cov(df['Volume']*volume_to_SI, enthalpy)[0, 1] / (k_B * temperature**2 * volume*volume_to_SI)
print(f'alpha_p:     {alpha_p:6.2e} K^-1')


# Print to csv file
with open('thermo.csv', 'w') as file:
    file.write(f'Temperature,Pressure,Volume,Enthalpy,c_p,kappa_T,alpha_p\n')
    file.write(f'{temperature},{pressure_SI},{volume_molar},{enthalpy.mean()},{c_p_molar},{kappa_T},{alpha_p}\n')


def run_avg(data, n):
    """ Box car average of data with n points """
    return np.convolve(data, np.ones(n)/n, mode='valid')

# Plot
plot_data = True

# Plot potential energy as a function of time using a box car average of n = 1000 points
if plot_data:
    df_all = thermo_data_as_dataframe(filename='../../../log-file/constant_pressure/log.otp', time_step=time_step, first_frame=0)
    n_boxcar = 2048

    # Make a function that replace the above code
    def plot_data(df_all, df, x, y, label, filename):
        plt.figure()
        plt.plot(run_avg(df_all[x], n_boxcar) * 1e9, run_avg(df_all[y], n_boxcar), 'k-', label='All data')
        plt.plot(run_avg(df[x], n_boxcar) * 1e9, run_avg(df[y], n_boxcar), 'r-', label='Selected for analysis')
        plt.xlabel('Time (ns)')
        plt.ylabel(label)
        plt.savefig(filename, dpi=300)


    plot_data(df_all, df, 'Time', 'PotEng', 'Potential energy (kcal/mol)', 'potential_energy.png')
    plot_data(df_all, df, 'Time', 'Volume', 'Volume (Å^3)', 'volume.png')

# Make a function that generate a LaTex file. It should have the PNG images, and a table with the computed values
#  (temperature, pressure, volume, enthalpy, c_p, kappa_T, alpha_p)
#  The table should have the values in SI units, and the units in parenthesis
def make_latex() -> str:
    """ Generate a LaTeX file with the results """
    latex = r"""
\documentclass{{article}}
\usepackage{{graphicx}}
\usepackage{{booktabs}}
\begin{{document}}
\begin{{table}}
\centering
\begin{{tabular}}{{ll}}
\toprule
Temperature & {temperature:6.0f} K \\
Pressure & {pressure:6.1f} atm \\
Volume & {volume:6.1f} $10^{{-6}}$m$^3$/mol \\
\hline
$c_P$ & {c_p:6.1f} J/mol/K \\
$\kappa_T$ & {kappa_T:6.2f} $10^{{-10}}$Pa$^{{-1}}$ \\
$\alpha_p$ & {alpha_p:6.2f} $10^{{-4}}$K$^{{-1}}$ \\
\hline
$K_T$ & {bulk_modulus:6.2f} GPa \\
\bottomrule
\end{{tabular}}
\end{{table}}
\begin{{figure}}
\centering
\includegraphics[width=0.8\textwidth]{{{{potential_energy.png}}}}
\includegraphics[width=0.8\textwidth]{{{{volume.png}}}}
\caption{{Time trajectories of energy and volume}}
\end{{figure}}
\end{{document}}
"""
    return latex.format(temperature=temperature,
                        pressure=pressure,
                        volume=volume_molar*1e6,
                        c_p=c_p_molar,
                        kappa_T=kappa_T*1e10,
                        alpha_p=alpha_p*1e4,
                        bulk_modulus=bulk_modulus/1e9)

with open('thermo.tex', 'w') as file:
    file.write(make_latex())

# Run LaTex
import subprocess
subprocess.run(['pdflatex', 'thermo.tex'])
