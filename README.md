# AquaMEND_salinity
**This is a process-based modeling framework that couples soil solution chemistry with microbial carbon cycling reactions to study the impacts of soil salinization.**
This framework considers both the direct and indirect effects of salinization. Indirect impacts include salinity-induced changes in solution chemistry, plant dynamics, and soil physicochemical properties. Direct impacts specifically influence microbially mediated carbon cycling processes, as depicted in a reaction network integrated into the AquaMEND model.


![Figure 1](https://github.com/user-attachments/assets/63459800-2746-4d78-9597-5af35544ec17)

This conceptual model is implemented numerically into the open-source geochemical program PHREEQC 3.0 (Parkhurst and Appelo, 2013). Follow the following steps to install PHREEQC

Step 1: PHREEQC installation (Mac system) Download is available on USGS website https://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/

In the .bash_profile under the home directory: export PATH="/Users/Jianqiu/Applications/phreeqc/bin:$PATH" export PHREEQC_DATABASE=/Users/Jianqiu/Applications/phreeqc/database/phreeqc.dat

Step 2: Copy and paste the database file (redox.dat) under the database directory

The soil solution chemistry is specified in the SOLUTION, GAS-PHASE, EXCHANGE, and SURFACE blocks. The reaction network is implemented using the KINETICS and RATES blocks. Salinity response functions are defined within the CALCULATE_VALUES block. Detailed guidelines for model implementation in PHREEQC are available in the user manual https://pubs.usgs.gov/tm/06/a43/
