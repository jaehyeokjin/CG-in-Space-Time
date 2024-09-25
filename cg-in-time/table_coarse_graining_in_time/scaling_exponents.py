#!/bin/python3

import pandas as pd

df = pd.read_csv('scaling_exponents.csv')

print(df)

df = df.drop(columns=['box_length'])

# Write to file as latex table
with open('scaling_exponents.tex', 'w') as f:
    f.write(df.to_latex(index=False, escape=False))

# Print LaTeX table to terminal
print(df.to_latex(index=False, escape=False))