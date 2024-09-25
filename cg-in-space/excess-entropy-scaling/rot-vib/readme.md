# `rot-vib' Folder analysis for excess entropy scaling

## Step 1. Vibrational Temperature
1. Run "parse_vib.py" to generate "vib.out" file from the "otp.sdf" file from the NIST database.
   -> The resultant vib.out contains the vibrational frequencies
2. At the given temperature (input), run "python partition_vib.py [TEMP]" to calculate the dimensionless ideal gas entropy for vibrational contribution. 
   -> The result is summarized in Table S3 in SI

## Step 2. Rotational Temperature
1. Self-explanatory (only three temperatures and can be readily converted through the SI information)

