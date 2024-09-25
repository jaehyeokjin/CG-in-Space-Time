import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

np.random.seed(2024)

x = np.linspace(0, 1, 512)
x_fast = np.linspace(0, 1, 64)
x_slow = np.linspace(0, 1, 8)

# y_slow fluctuations
y_slow_points = np.random.random(len(x_slow))-0.5
y_slow = interp1d(x_slow, y_slow_points, kind='cubic')

# y_fast fluctuations
y_fast_points = np.random.random(len(x_fast))-0.5
y_fast = interp1d(x_fast, y_fast_points, kind='cubic')

# y_fast fluctuations
y2_fast_points = np.random.random(len(x_fast))-0.5
y2_fast = interp1d(x_fast, y2_fast_points, kind='cubic')

vertical_scale_factor = 0.4

plt.figure(figsize=(4, 4))
plt.rcParams.update({
    'font.family': 'Whitney Book'
})
plt.subplot(2, 1, 1)
plt.plot(x, y_slow(x) + vertical_scale_factor * y_fast(x), 'k-', label='Slow')
plt.plot(x, y_slow(x), 'r-', lw='4',label='Slow')
plt.xticks([])
plt.yticks([])
plt.xlim(0, 1)
plt.text(0.02, 0.08, '(a)', transform=plt.gca().transAxes, fontsize=16)
plt.text(0.84, 0.08, r'${\bf r}_1$', transform=plt.gca().transAxes, fontsize=16)
plt.ylabel('Potential energy', fontsize=14)

plt.subplot(2, 1, 2)
horizontal_scale_factor = 1.10
x_scaled = x * horizontal_scale_factor
plt.plot(x_scaled, y_slow(x) + vertical_scale_factor * y2_fast(x), 'k-', label='Slow')
plt.plot(x_scaled, y_slow(x), 'r-', lw='4',label='Slow')
plt.xticks([])
plt.yticks([])
plt.xlim(0, 1)
plt.text(0.02, 0.08, '(b)', transform=plt.gca().transAxes, fontsize=16)
plt.text(0.63, 0.80, r'${\bf r}_2 = \lambda{\bf r}_1$', transform=plt.gca().transAxes, fontsize=16)
plt.ylabel('Potential energy', fontsize=14)

plt.xlabel(r'System coordinate, ${\bf r}$',fontsize=16)

# Remove horizontal space between axes
plt.subplots_adjust(hspace=0)

plt.savefig('figure_energy_landscape.png', dpi=300, bbox_inches='tight')
plt.savefig('figure_energy_landscape.pdf', dpi=600, bbox_inches='tight')
plt.show()
