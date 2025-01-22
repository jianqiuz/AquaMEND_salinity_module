# AquaMEND_salinity
**This is a process-based modeling framework that couples soil solution chemistry with microbial carbon cycling reactions to study the impacts of soil salinization.**


![Figure 1](https://github.com/user-attachments/assets/63459800-2746-4d78-9597-5af35544ec17){width=400px}

This conceptual model is implemented numerically into the open-source geochemical program PHREEQC 3.0 (Parkhurst and Appelo, 2013).

@@ -12,3 +14,4 @@ Follow the following steps to install PHREEQC

* Step 2: Copy and paste the database file (redox.dat) under the database directory

The soil solution chemistry is specified in the SOLUTION, GAS-PHASE, EXCHANGE, and SURFACE blocks. The reaction network is implemented using the KINETICS and RATES blocks. Salinity response functions are defined within the CALCULATE_VALUES block. Detailed guidelines for model implementation in PHREEQC are available in the user manual https://pubs.usgs.gov/tm/06/a43/
