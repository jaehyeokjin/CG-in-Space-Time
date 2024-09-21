# Data repository for 'Thermodynamic Scaling in Molecular Liquids: Coarse-Graining in Space and Time'
Zenodo link: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11624467.svg)](https://doi.org/10.5281/zenodo.11624467)

Authors:
* Jaehyeok Jin (jj3296@columbia.edu)
* David R. Reichman (drr2103@columbia.edu)
* Jeppe C. Dyre (dyre@ruc.dk)
* Ulf R. Pedersen (urp@ruc.dk)

Preprint: [arXiv:2402.08675](https://arxiv.org/abs/2402.08675)

## Folders

Below is a description of the folders in this repository.
The folders contain data, figures, and Python scripts necessary to generate the figures depicted in the manuscript.
Separately, we arcivhed the log files (2.9 GB) in `log-file` for analyzing the simulation data. The input scripts are provided in the `cg-in-time` or `cg-in-space` folder to generate these log files if needed, while the `ipynb` Jupyter notebook is designed to read the log files from the log folder by default.

### Temporal Coarse Graining: under folder `cg-in-time`

1. Folder `constant_pressure`: Figure 14
    1. Contains data for the constant pressure (and temperature) simulations.
    2. Input files are included in this folder, where the full log files are separately provided in `./log-file/constant_pressure`.
    3. These are used to compute the Prigogine-Defay ratio (plotted in Fig. 14) by running `plot_data.py`.

2. Folder `constant_volume`: Figures 2, 15
    1. Contains simulation snapshots and state point information (refer to `msd.py` for detailed T and rho conditions) for Fig. 2.
    2. Contains data for the constant volume simulations used to compute the diffusion coefficient (`*.csv` files in the subfolders).
    3. Run `msd.py` with \gamma=6.5 to arrive at the scaling relationship (Fig. 15).

3. Folder `figure_energy_landscape`: Figure 1
    1. Script for making a conceptual illustration of an energy landscape (Fig. 1).

4. Folder `T380_L35.944` (Main analysis folder): Figures 4-8, S1. The folder does not contail LAMMPS log files, but can be created (see README files in folders) or referred to `./log-file/T380_L35.944'.
    1. PEDAGOGICAL GUIDE: `coarse-graining-in-time.ipynb`
        1. Detailed introduction to coarse-graining in time, based on the time-averaging described in the paper. This folder includes a pedagogical Jupyter notebook for the CG in time approach that reads the log file from the log folder `./log-file/T380_L35.944`.
        2. Based on the SciPy implementation described in the paper, `coarse-graining-in-time.ipynb` provides a comprehensive guideline for performing temporal coarse-graining with detailed comments about the implementation at this single state point. (See 4.2 below)
    2. MAIN ANALYSIS: `analyse.py` and `analyse.ipynb`
        1. This folder contains the `analyse.ipynb` Jupyter notebook, which performs comprehensive analysis using the driver `analyse.py` described in the manuscript. This analysis file also reads the same log file from `./log-file/T380_L35.944`.
        2. While this analysis is performed at T=380K and box length L=35.944, corresponding to ambient pressure, the script provided in this folder can be readily applied to other thermodynamic state points described in 2.1.
        3. Error-bar analysis is available.
            1. Running `analyse.ipynb` in the `T380_L35.944` folder gives a single value. 4.2.3.2 For error bar analysis, run `figures_for_manuscript.ipynb` in the `error_bar_T380_L35.944` folder. This divides the trajectory into 8 pieces and performs the block-averaging method. Note that all ipynb files here currently use the log files in the log folder, or can be generated from the input file provided.
            2. This error bar analysis script generates the temporal coarse-grained results: Figs. 4-8, S1.

5. Folder `table_coarse_graining_in_time`: Table 1
    1. Contains Table 1 from the manuscript.
6. Folder `lennard-jones`: Figs. S4-S6
    1. AUXILIARY ANALYSIS: `lennard_jones.ipynb`
        1. This Jupyter notebook provides auxiliary analysis for extending temporal coarse-graining to complex interaction profile systems (Lennard-Jones).
        2. Detailed explanations are provided within the `*.ipynb` file and generate Figures S4-S6 described in the Supplemental Material.
        3. Input files and data files for LAMMPS are provided here to generate log file needed for analysis. Alternatively, refer to `./log-file/lennard-jones/

### Spatial Coarse Graining: under the folder `cg-in-space`

7. `coarse-graining`: This folder contains the essential scripts/results from spatial coarse-graining of OTP molecules.
    For naming conventions in 7.1.1 and 7.1.2 below, refer to `statepoint.in` for state point information (contains labels #1-#23).
    1. `cg-interaction`: Figures 10, S2
        1. Contains the spatial CG interaction (`.table`) obtained from OpenMSCG (https://software.rcc.uchicago.edu/mscg/).
        2. Running `plot.gnuplot` in gnuplot will generate `*.png` subfigures.
        3. Compiling them together will create `trim-cg-interaction.pdf` (Fig. 10) and `full-cg-interaction.pdf` (Fig. S2) in the `final-figure` folder.

    2. `cg-rdf` and `ref-rdf`: Figures 11, S3
    These folders contain the COM RDF from CG simulation (`cg-rdf`) and mapped FG simulation (`ref-rdf`).
        1. RDF files follow the `*.rdf` file format.
        2. Running `plot.gnu` in gnuplot from the `cg-rdf` folder will generate `*.png` subfigures.
        3. Compiling them together will create `trim-OTP-RDF.pdf` (Fig. 11) and `full-OTP-RDF.pdf` (Fig. S3) in the `final-figure` folder.

    3. `lewis-wahnstrom`: Figure 12
        1. This folder contains the necessary results/analysis required for Figure 12.
        2. `Interaction`
            1. Contains Figure 12(a), (b), and (c) subfigures.
        3. `RDF`
            1. Contains Figure 12(d) subfigures (COM level RDF values).

    4. `power-spectrum`: Figure 17
        1. `aa` and `cg` folders contain results from 2PT simulations (power spectrum files).
        2. Running `plot.gnuplot` in gnuplot will generate Fig. 17.

8. Folder `scaling-exponent`: Figure 13
    1. 2PT simulation results are listed as `2pt.out`
    2. Contains comprehensive 2PT simulation results for scanning the excess entropy/computing them throughout various state points are available in `./log-file/2pt`
        1. Box length: 35, 35.5, 36, 36.5, 37, 37.5, 38 (\AA)
        2. Temperature: 400, 420, 440, 460, 480, 500, 540, 600, 700 (K)
    3. ANALYSIS: `Spatial CG Gamma.ipynb` Jupyter notebook imports these results and generates Figure 13 for the scaling exponent.

9. Folder `excess-entropy-scaling`
    1. `rot-vib`
        1. This folder calculates the rotational and vibrational temperatures listed in the Supplemental Material.
        2. The `README` file in this folder provides detailed step-by-step instructions, starting from importing the `otp.sdf` file and running the Python scripts included there.
        3. OTP.SDF file is obtained from : https://webbook.nist.gov/cgi/cbook.cgi?ID=C84151
    2. `scaling-relationship`: Figure 16
        1. Using the results from 8.1, this folder provides the analysis to perform excess entropy scaling (Fig. 16).
        2. Reading `result.out` and generating `fg_sex_scaling.png` abd `pdf` files.
        3. A step-by-step guide is provided in the Jupyter notebook `entropy_scaling.ipynb`.
