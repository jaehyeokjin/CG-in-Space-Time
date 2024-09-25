import scipy.constants as const

# Constants
epsilon_kJ_mol = 0.997  # in kJ/mol
sigma_nm = 0.34         # in nm
density_mol_L = 34.6    # in mol/L
temperature_K = 80      # in K

print(f'{density_mol_L=}')
print(f'{temperature_K=}')

# Convert epsilon to Joules per molecule
epsilon_J = epsilon_kJ_mol * 1e3 / const.Avogadro

# Convert sigma to meters
sigma_m = sigma_nm * 1e-9

# Convert density to number per m^3
density_m3 = density_mol_L * 1e3 * const.Avogadro

# Calculate reduced temperature T*
T_star = const.Boltzmann * temperature_K / epsilon_J
print(f'{T_star=}')

# Calculate reduced density rho*
rho_star = density_m3 * sigma_m**3
print(f'{rho_star=}')


