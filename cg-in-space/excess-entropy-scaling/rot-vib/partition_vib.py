import sys
import numpy as np

def convert_cm1_to_kelvin(frequency_cm1):
    """ Convert wavenumber in cm^-1 to temperature in Kelvin """
    h = 6.62607015e-34  # Planck's constant in joule*seconds
    c = 2.998e10         # Speed of light in cm/s
    kB = 1.380649e-23    # Boltzmann's constant in joule/Kelvin
    frequency_hz = frequency_cm1 * c
    energy_j = h * frequency_hz
    return energy_j / kB

def partition_function(theta, T):
    """ Calculate the vibrational partition function component for a single mode """
    term1 = theta / T / (np.exp(theta / T) - 1)
    term2 = -np.log(1 - np.exp(-theta / T))
    return term1 + term2

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <temperature>")
        return

    T = int(sys.argv[1])  # Temperature provided via command line
    vibrational_frequencies = []

    # Read the first column from each line in 'vib.out'
    with open('vib.out', 'r') as file:
        for line in file:
            first_column = line.strip().split()[0]
            vibrational_frequencies.append(float(first_column))

    # Convert frequencies to Kelvin and calculate partition function
    partition_sum = 0
    for frequency_cm1 in vibrational_frequencies:
        theta = convert_cm1_to_kelvin(frequency_cm1)
        partition_sum += partition_function(theta, T)

    print("Total Vibrational Partition Function:", partition_sum)

if __name__ == "__main__":
    main()

