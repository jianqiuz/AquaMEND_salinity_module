# AquaMEND_salinity
**This is a process-based modeling framework that couples soil solution chemistry with microbial carbon cycling reactions to study the impacts of soil salinization.**
This framework considers both the direct and indirect effects of salinization. Indirect impacts include salinity-induced changes in solution chemistry, plant dynamics, and soil physicochemical properties. Direct impacts specifically influence microbially mediated carbon cycling processes, as depicted in a reaction network integrated into the AquaMEND model.


![Figure 1](https://github.com/user-attachments/assets/63459800-2746-4d78-9597-5af35544ec17)

This conceptual model is implemented numerically into the open-source geochemical program PHREEQC 3.0 (Parkhurst and Appelo, 2013). The model is designed to simulate key microbial and geochemical processes in soils. 

**`Step 1:'** PHREEQC installation (Mac system) Download is available on USGS website https://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/  
-Extract and install PHREEQC in a preferred directory (e.g.,  /usr/local/phreeqc)  
-Open the terminal and update the .bash_profile  
-Add the following lines (replace XX with your PHREEQC installzaton path:  
export PATH="XX/phreeqc/bin:$PATH"   
export PHREEQC_DATABASE=XX/phreeqc/database/phreeqc.dat  
-Save the file and apply the changes  
-To verify installation, run "phreeqc" in the terminal, if the installation is successful, you should see the prompt "Name of input file?" 
  
**`Step 1:'** Copy and paste the database file (redox.dat) provided in the database folder to your PHREEQC database directory  

The soil solution chemistry is specified in the SOLUTION, GAS-PHASE, EXCHANGE, and SURFACE blocks. The reaction network is implemented using the KINETICS and RATES blocks. Salinity response functions are defined within the CALCULATE_VALUES block. Detailed guidelines for model implementation in PHREEQC are available in the user manual https://pubs.usgs.gov/tm/06/a43/

### File Dictionary

- **`AquaMEND_microbial_mechanisms`**: Contains model setup and simulations for testing various microbial process-based hypotheses related to soil salinization, including microbial mortality, carbon use efficiency (CUE), extracellular enzyme activity, and other microbial mechanisms. Exactuable input files have a .phrq extension, while detailed output files are saved as .phrq.out, Extracted outputs are written to .txt files as specified in the input script.

- **`AquaMEND_process_couple`**: Includes model setup and simulations for exploring coupled biotic-abiotic processes and their interactions.

- **`AquaMEND_Redox`**: Focuses on model setup and simulations to evaluate shifts among key redox processes, such as aerobic respiration, sulfate reduction, and methanogenesis.

- **`AquaMEND_salinity_buffer`**: Contains model setup and simulations to assess the impact of three different cation exchange and surface complexation processes on salinity buffering.

- **`AquaMEND_sorption`**: Provides model setup and simulations for investigating the effects of salinity on dissolved organic matter (DOM) sorption and desorption processes.

- **`data`**: Includes datasets used to develop salinity response functions and evaluate salinity buffering capacity.



- **`database`**: Contains the `.dat` file required by PHREEQC for model execution. 



