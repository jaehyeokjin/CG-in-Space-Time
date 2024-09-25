import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Seed seed for random number generator
np.random.seed(2023)

# Read data from csv file
df = pd.read_csv('thermo.csv').sort_values(by=['Temperature'])
df_all = df.copy()

# Remove temperature in remove_invervals
remove_intervals = [(210, 230), (310, 350), (500, 600)]
for interval in remove_intervals:
    df = df[(df['Temperature']<interval[0]) | (df['Temperature']>interval[1])]

# Function to fit straight line, find slope and intercept for x<x_max, and values of y for x_fit
def fit_line(x: np.ndarray, y: np.ndarray, x_fit: np.ndarray) -> np.ndarray:
    slope, intercept = np.polyfit(x, y, 1)
    y_fit = slope*x_fit + intercept
    return y_fit

def fit_line_error_estimate(x: np.ndarray, y: np.ndarray, x_fit: float) -> (float, float):
    from scipy import stats
    # Fit straight line
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    # Predicted value of y at x_fit
    y_fit = slope * x_fit + intercept

    # Calculate mean squared error
    residuals = y - (slope * x + intercept)
    mean_squared_err = np.mean(residuals ** 2)

    # Standard Error of the prediction
    n = len(x)
    x_bar = np.mean(x)
    std_err_of_prediction = np.sqrt(std_err ** 2 + mean_squared_err * (1 + 1 / n + ((x_fit - x_bar) ** 2) / np.sum((x - x_bar) ** 2)))

    # Calculate the confidence interval
    confidence_interval = 0.67
    t_value = stats.t.ppf((1 + confidence_interval) / 2, len(x) - 2)
    ci_lower = y_fit - t_value * std_err_of_prediction
    ci_upper = y_fit + t_value * std_err_of_prediction

    # Calculate the error estimate
    y_fit_error = (ci_upper - ci_lower) / 2

    return y_fit, y_fit_error

def monte_carlo_error_estimate(func, input_means, input_standard_deviations, n_samples=1000):
    """ Assume that inputs are gaussian distributed with mean and standard deviation.
    Return the mean and standard deviation of the output of the function func.
    """
    # Generate n_samples random numbers for each input
    n_inputs = len(input_means)
    inputs = np.zeros((n_samples, n_inputs))
    for i in range(n_inputs):
        inputs[:, i] = np.random.normal(input_means[i], input_standard_deviations[i], n_samples)
    # Calculate the output
    outputs = func(*inputs.T)
    # Return the mean and standard deviation of the output
    return np.mean(outputs), np.std(outputs)

print(df)

T_glass = 350
glass = df[df['Temperature']<T_glass]
liquid = df[df['Temperature']>T_glass]

plt.figure(figsize=(5, 5))
plt.rcParams.update({
    'font.family': 'DejaVu Sans',   # Default font
    #'font.family': 'Whitney Book', # Actual font used in the paper (needs to install font first)
})
plt.subplot(2, 2, 2)
plt.plot(df['Temperature'], df['c_p'], 'bo')
plt.plot(df_all['Temperature'], df_all['c_p'], 'o', markerfacecolor='none', markeredgecolor='b')
# Find extrapolated value of c_p of glass at T_glass
c_p_glass, c_p_glass_error = fit_line_error_estimate(glass['Temperature'], glass['c_p'], T_glass)
plt.errorbar(T_glass, c_p_glass, yerr=c_p_glass_error, fmt='r', capsize=4)
x_fit = np.linspace(150, T_glass, 8)
plt.plot(x_fit, fit_line(glass['Temperature'], glass['c_p'], x_fit), 'r--')
# Find extrapolated value of c_p of liquid at T_glass
c_p_liquid, c_p_liquid_error = fit_line_error_estimate(liquid['Temperature'], liquid['c_p'], T_glass)
plt.errorbar(T_glass, c_p_liquid, yerr=c_p_liquid_error, fmt='g', capsize=4)
x_fit = np.linspace(T_glass, 550, 8)
plt.plot(x_fit, fit_line(liquid['Temperature'], liquid['c_p'], x_fit), 'g--')
delta_c_p, delta_c_p_error = monte_carlo_error_estimate(lambda x, y: x - y, [c_p_liquid, c_p_glass], [c_p_liquid_error, c_p_glass_error])
print(f'delta_c_p = {delta_c_p:3.0f} +- {delta_c_p_error:3.0f} J/mol/K')
plt.text(190, 880, r'$\Delta c_P$ = ' f'{delta_c_p:3.0f}({delta_c_p_error:1.0f})' r' J/mol$\cdot$K', fontsize=10)
plt.xlabel('Temperature (K)')
plt.ylabel(r'$c_p$ (J/mol$\cdot$K)')
plt.xlim(150, 480)
plt.ylim(870, 1020)
plt.xticks([])
# Axis on the right
plt.gca().yaxis.tick_right()
plt.gca().yaxis.set_label_position("right")
plt.text(0.04, 0.88, '(b)', transform=plt.gca().transAxes, fontsize=12)

plt.subplot(2, 2, 3)
plt.plot(df['Temperature'], df['kappa_T']*1e10, 'bo')
plt.plot(df_all['Temperature'], df_all['kappa_T']*1e10, 'o', markerfacecolor='none', markeredgecolor='b')
# Find extrapolated value of bulk modulus of glass at T_glass
kappa_glass, kappa_glass_error = fit_line_error_estimate(glass['Temperature'], glass['kappa_T'], T_glass)
plt.errorbar(T_glass, kappa_glass*1e10, yerr=kappa_glass_error*1e10,  fmt='r', capsize=4)
x_fit = np.linspace(150, T_glass, 8)
plt.plot(x_fit, fit_line(glass['Temperature'], glass['kappa_T'], x_fit) * 1e10, 'r--')
# Find extrapolated value of bulk modulus of liquid at T_glass
kappa_liquid, kappa_liquid_error = fit_line_error_estimate(liquid['Temperature'], liquid['kappa_T'], T_glass)
plt.errorbar(T_glass, kappa_liquid*1e10, yerr=kappa_liquid_error, fmt='g', capsize=4)
x_fit = np.linspace(T_glass, 550, 8)
plt.plot(x_fit, fit_line(liquid['Temperature'], liquid['kappa_T'], x_fit) * 1e10, 'g--')
delta_kappa, delta_kappa_error = monte_carlo_error_estimate(lambda x, y: x - y, [kappa_liquid, kappa_glass], [kappa_liquid_error, kappa_glass_error])
print(f'delta_kappa = {delta_kappa*1e10:3.3f} +- {delta_kappa_error*1e10:1.3f} Pa^-1')
plt.text(170, 0.5, r'$\Delta \kappa_T$ = ' f'{delta_kappa*1e10:3.2f}({delta_kappa_error*1e12:1.0f})' r'$\times$ 10$^{-10}$ Pa$^{-1}$', fontsize=9)
plt.xlabel('Temperature (K)')
plt.ylabel(r'$\kappa_T$ (10$^{-10}$ Pa$^{-1}$)')
plt.yticks([0, 2, 4, 6, 8, 10])
plt.xlim(150, 480)
plt.ylim(0, 9)
plt.text(0.04, 0.88, '(c)', transform=plt.gca().transAxes, fontsize=12)

plt.subplot(2, 2, 4)
plt.plot(df['Temperature'], df['alpha_T']*1e4, 'bo')
plt.plot(df_all['Temperature'], df_all['alpha_T']*1e4, 'o', markerfacecolor='none', markeredgecolor='b')
# Find extrapolated value of the expansion coefficient of glass at T_glass
alpha_glass, alpha_glass_error = fit_line_error_estimate(glass['Temperature'], glass['alpha_T'], T_glass)
plt.errorbar(T_glass, alpha_glass*1e4, yerr=alpha_glass_error*1e4, fmt='r', capsize=4)
x_fit = np.linspace(150, T_glass, 8)
plt.plot(x_fit, fit_line(glass['Temperature'], glass['alpha_T'], x_fit) * 1e4, 'r--')
# Find extrapolated value of the expansion coefficient of liquid at T_glass
alpha_liquid, alpha_liquid_error = fit_line_error_estimate(liquid['Temperature'], liquid['alpha_T'], T_glass)
plt.errorbar(T_glass, alpha_liquid * 1e4, yerr=alpha_liquid_error * 1e4, fmt='g', capsize=4)
x_fit = np.linspace(T_glass, 550, 8)
plt.plot(x_fit, fit_line(liquid['Temperature'], liquid['alpha_T'], x_fit) * 1e4, 'g--')
delta_alpha, delta_alpha_error = monte_carlo_error_estimate(lambda x, y: x - y, [alpha_liquid, alpha_glass], [alpha_liquid_error, alpha_glass_error])
print(f'delta_alpha = {delta_alpha*1e4:3.3f} +- {delta_alpha_error*1e4:1.3f} K^-1')
plt.text(165, 0.6, r'$\Delta \alpha_p$ = ' f'{delta_alpha*1e4:3.2f}({delta_alpha_error*1e6:1.0f})' r'$\times$ 10$^{-4}$ K$^{-1}$', fontsize=10)
plt.xlabel(r'Temperature, $T$ (K)')
plt.ylabel(r'$\alpha_p$ (10$^{-4}$ K$^{-1}$)')
plt.xlim(150, 480)
plt.ylim(0, 9)
plt.ylim(0, None)
plt.gca().yaxis.tick_right()
plt.gca().yaxis.set_label_position("right")
plt.text(0.04, 0.88, '(d)', transform=plt.gca().transAxes, fontsize=12)


# Volume
plt.subplot(2, 2, 1)
plt.plot(df['Temperature'], df['Volume']*1e6, 'bo')
plt.plot(df_all['Temperature'], df_all['Volume']*1e6, 'o', markerfacecolor='none', markeredgecolor='b')
# Find extrapolated value of the volume of glass at T_glass
volume_glass, volume_glass_error = fit_line_error_estimate(glass['Temperature'], glass['Volume'], T_glass)
#plt.plot(T_glass, volume_glass*1e6, 'rd')
x_fit = np.linspace(150, T_glass-20, 8)
plt.plot(x_fit, fit_line(glass['Temperature'], glass['Volume'], x_fit) * 1e6, 'r--')
# Find extrapolated value of the volume of liquid at T_glass
volume_liquid, volume_liquid_errpr = fit_line_error_estimate(liquid['Temperature'], liquid['Volume'], T_glass)

#plt.plot(T_glass, volume_liquid*1e6, 'gd')
x_fit = np.linspace(T_glass, 550, 8)
plt.plot(x_fit, fit_line(liquid['Temperature'], liquid['Volume'], x_fit) * 1e6, 'g--')
delta_volume = volume_liquid - volume_glass
#plt.text(160, 220, r'$\Delta V$ = ' f'{delta_volume*1e6:3.2f} ' r'cm$^3$/mol', fontsize=10)
#plt.xlabel('Temperature (K)')
plt.ylabel(r'Volume (cm$^3$/mol)')
plt.xlim(150, 480)
plt.ylim(205, 250)
plt.xticks([])
# Prigogine-Defay ratio:
# \Pi = \frac{\Delta c_p \cdot \Delta \kappa_T}{T_g \cdot V_g \cdot (\Delta \alpha_T)^2}
Pi_old = delta_c_p * delta_kappa / (T_glass * volume_liquid * delta_alpha**2)
T_glass_error = 10
V_glass: float = volume_liquid
V_glass_error = V_glass * 0.01
print(f'Pi_old = {Pi_old:3.2f}')
Pi, Pi_error = monte_carlo_error_estimate(lambda c, kappa, alpha, T, V: c * kappa / (T * V * alpha ** 2), [delta_c_p, delta_kappa, delta_alpha, T_glass, V_glass], [delta_c_p_error, delta_kappa_error, delta_alpha_error, T_glass_error, V_glass_error])
print(f'Pi = {Pi:3.2f} +- {Pi_error:3.2f}')
plt.text(170, 238, r'$T_g=$' f'{T_glass:3.0f}({T_glass_error:1.0f}) K', fontsize=10)
plt.text(170, 233, r'$V_g$ = ' f'{volume_liquid*1e6:3.0f}({V_glass_error*1e6:1.0f}) ' r'cm$^3$/mol', fontsize=10)
plt.text(170, 220, r'$\Pi$ = ' f'{Pi:3.2f}({Pi_error*1e2:1.0f})', fontsize=11)
plt.text(0.04, 0.88, '(a)', transform=plt.gca().transAxes, fontsize=12)
plt.text(390, 208, '1 atm', fontsize=10)

plt.subplots_adjust(hspace=0.0)
plt.subplots_adjust(wspace=0.0)
plt.gcf().align_ylabels()
plt.savefig('prigogine_defay.pdf', dpi=300, bbox_inches='tight')
plt.savefig('prigogine_defay.png', dpi=300, bbox_inches='tight')
plt.show()

# Experimental density
ambient_temperature = 298  # K
molar_mass = 230.3  # g/mol
rho_exp = 1.16  # g/cm^3
molar_volume_exp = molar_mass/rho_exp
plt.plot([ambient_temperature], [molar_volume_exp], 'kx', markersize=10)
plt.text(ambient_temperature-10, molar_volume_exp+2, 'Exp.', fontsize=12)
print(f'Experimental molar volume: {molar_volume_exp:3.0f} cm^3/mol')

print(df.columns)
