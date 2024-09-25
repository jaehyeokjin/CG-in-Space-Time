import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def parse_jcamp(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    xfactor = yfactor = 1.0
    deltax = 1.0
    x_start = 0.0
    y_data = []
    x_data = []
    
    for line in lines:
        if line.startswith('##XFACTOR='):
            xfactor = float(line.split('=')[1].strip())
        elif line.startswith('##YFACTOR='):
            yfactor = float(line.split('=')[1].strip())
        elif line.startswith('##DELTAX='):
            deltax = float(line.split('=')[1].strip())
        elif line.startswith('##FIRSTX='):
            x_start = float(line.split('=')[1].strip())
        elif line.startswith('##XYDATA='):
            xy_data_section = lines[lines.index(line) + 1:]  # XY data starts after this line
            current_x = x_start
            for data_line in xy_data_section:
                parts = data_line.strip().split()
                x_value = float(parts[0])
                y_values = [float(y) * yfactor for y in parts[1:]]
                x_values = [x_value + i * deltax for i in range(len(y_values))]
                x_data.extend(x_values)
                y_data.extend(y_values)
                current_x += deltax * len(y_values)
    return np.array(x_data), np.array(y_data)

def detect_peaks(x, y, height=None, distance=50):
    peaks, _ = find_peaks(y, height=height, distance=distance)
    return x[peaks], y[peaks]

def plot_spectrum(x, y, peak_x, peak_y):
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label='IR Spectrum')
    plt.scatter(peak_x, peak_y, color='red', s=40, label='Peaks')
    plt.title('IR Spectrum with Identified Peaks')
    plt.xlabel('Wavenumber (1/cm)')
    plt.ylabel('Absorbance')
    plt.legend()
    plt.show()

# Example usage
filename = 'otp.jdx'  # Path to your JCAMP-DX file
x, y = parse_jcamp(filename)
peak_x, peak_y = detect_peaks(x, y, height=0.1)  # Adjust 'height' based on your data
plot_spectrum(x, y, peak_x, peak_y)

