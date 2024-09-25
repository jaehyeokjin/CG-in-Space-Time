#!/bin/python3

from glob import glob

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import constants
from scipy.interpolate import interp1d

plt.style.use('classic')

directories = glob('T700*')
directories += glob('T600*')
directories += glob('T540*')
directories += glob('T500*')
directories += glob('T480*')
directories += glob('T460*')
directories += glob('T450*')
directories += glob('T440*')
directories += glob('T420_L??.???')
directories += glob('T400*')
#directories += glob('T330_L35.5')
#directories += glob('T400*')
directories += glob('T380_L35.944_c0')

directories.sort()
print(directories)

plt.figure(figsize=(8, 8))
data = []
for directory in directories:
    T = float(directory.replace('T','').replace('_', ' ').split()[0])
    L = float(directory.replace('L','').replace('_', ' ').split()[1])
    filename=f'{directory}/mean_squared_displacement.csv'
    df = pd.read_csv(filename)
    ii = int(len(df.MSD)/2)
    D = np.mean(df.MSD[:ii])/np.mean(df.Time[:ii])/6
    print(D)
    plt.plot(df.Time, df.MSD, 'o', label=f'{directory}, {D = :.2f}')
    plt.plot(df.Time, 6*D*df.Time, 'k--')
    
    filename=f'{directory}/thermo_stats.csv'
    thermo_stats = pd.read_csv(filename, index_col=0)
       
    data.append({
        'Temperature': T,
        'Pressure': thermo_stats['Press']['mean'],
        'Density': thermo_stats['Density']['mean'],
        'Box_Length': L,
        'Number_Density': 125/L**3,
        'Diffusion_Coefficient': D,
        'directory': directory
    })
plt.xlabel(r'Time, $t$ [ns]')
plt.ylabel(r'Mean Squared Displacement [$\AA^3$]')
plt.xscale('log')
plt.yscale('log')
plt.ylim(1e-2, None)
plt.xlim(None, 1e4)
plt.legend(loc='lower right', fontsize=10)
plt.show()


df = pd.DataFrame(data)
print(df)

df.to_csv('ortho_terphenyl.csv', index=False)

#u = constants.physical_constants['atomic mass constant'][0]
N_A = constants.Avogadro
molecular_mass = 230.3e-3/N_A
print(molecular_mass)
l_0 = df.Number_Density**(-1/3)  # In Angstrom
t_0 = (molecular_mass/constants.Boltzmann/df.Temperature)**0.5*(l_0*1e-10)*1e9  # in nanoseconds
print(f'{l_0[0] = }, {t_0[0] = }')
df['Reduced_Diffusion_Coefficient'] = df.Diffusion_Coefficient*t_0/l_0**2
cmap = plt.cm.get_cmap('rainbow')

plt.figure(figsize=(8, 5))
plt.rcParams.update({
    'font.family': 'DejaVu Sans',   # Default font
    #'font.family': 'Whitney Book', # Actual font used in the paper (needs to install font first)
})
gamma = 6.5
Gamma = 1000*df.Density**gamma/df.Temperature
sc = plt.scatter(Gamma, 1/df.Reduced_Diffusion_Coefficient, c=df.Temperature, s=100, cmap=cmap)
#plt.plot([0, 5], np.array([2e2, 5e4])*1.1, 'k:', lw=3)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.xlabel(r'$1000\rho^\gamma/T$ [(g/ml)$^\gamma/K$]', fontsize=20)
plt.xlim(0, 5)
plt.ylim(3e2, 2e5)
plt.ylabel(r'Reduced Inverse Diffusion Coefficient' '\n' r'$1/\tilde D=l_0^2/Dt_0$',fontsize=20)
cbar = plt.colorbar(sc)
cbar.set_label('Temperature [K]', fontsize=20)
cbar.ax.tick_params(labelsize=16)

plt.yscale('log')
plt.text(3.3, 5e2, r'$\gamma=$' f'{gamma:0.1f}', fontsize=25)
plt.savefig('density_scaling_otp.pdf', dpi=600, bbox_inches='tight')
plt.savefig('density_scaling_otp.png', dpi=300, bbox_inches='tight')
plt.show()

# Figure with investigated state points
plt.figure(figsize=(4, 4))
plt.rcParams.update({
    'font.family': 'DejaVu Sans',   # Default font
    #'font.family': 'Whitney Book', # Actual font used in the paper (needs to install font first)
})
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.scatter(df.Temperature, df.Density, c=df.Temperature, s=100)
spline_points = ((350, 450, 650), (1.055, 0.977, 0.85))
f = interp1d(*spline_points, kind='quadratic')
x_vals = np.linspace(min(spline_points[0]), max(spline_points[0]), 100)
plt.plot(x_vals, f(x_vals), 'k--', lw=3)
# plt.plot(*spline_points, '+', lw=5)
plt.text(400, 0.97, r'$p=1$ atm', fontsize=18, rotation=-43)
plt.text(0.05, 0.87, '(b)', transform=plt.gca().transAxes, fontsize=20)
plt.xlim(350, 725)
plt.ylim(0.825, 1.15)
plt.xlabel(r'$T$ [K]', fontsize=20)
plt.ylabel(r'$\rho$ [g/ml]', fontsize=20)
plt.savefig('density_temperature_otp.pdf', dpi=600, bbox_inches='tight')
plt.savefig('density_temperature_otp.png', dpi=300, bbox_inches='tight')
plt.show()

