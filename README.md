# Backward Facing Step Simulation with OpenFOAM and Python Automation

## Overview
This project automates the setup and execution of a Backward Facing Step simulation using OpenFOAM. The simulation setup, boundary conditions, and physical properties are configured using a Python script, while a Bash script is provided to automate the entire simulation workflow, including mesh generation, running the simulation, and generating visualizations.

This project not only automates the setup and execution of a Backward Facing Step simulation using OpenFOAM but also lays the foundation for conducting ensemble simulations and uncertainty quantification (UQ) studies. The ability to systematically modify simulation parameters via Python scripts enables researchers to explore the parameter space efficiently, making this approach particularly useful for computational studies requiring high-throughput simulations.

**Author:** Palak Patel

### Key Components:
1. **Python Scripts for Simulation Setup**
    - **`run_simulation.py`**: This Python module provides functions to automate the setup of an OpenFOAM simulation
    - **`test_simulation_setup.py`**: This script uses the functions from `run_simulation.py` to configure the simulation for the Backward Facing Step case. It updates boundary conditions, turbulence models, and control parameters.

2. **Paraview Script for Visualization**
    - **`state.py`**: A ParaView script to generate visualizations of the simulation results. This script uses ParaView's offscreen rendering mode to produce visual output files.

3. **Bash Script for Simulation Execution**
   - **`simulate.sh`**: This Bash script automates the entire process of running the simulation. It sets up the simulation directory, generates the mesh, runs the SIMPLE algorithm, and creates visualizations using ParaView.

## File Structure

```bash
├── backwardFacingStep_template/        # Template directory containing base OpenFOAM setup
├── run_simulation.py                   # Python module for setting up the simulation
├── test_simulation_setup.py            # Python script for configuring simulation parameters
├── simulate.sh                         # Bash script to automate the entire simulation
└── README.md                           # Project documentation
```

## Prerequisites

- **OpenFOAM**: For CFD simulation. Ensure that the `blockMesh` and `simpleFoam` utilities are accessible.
- **ParaView**: For generating visualizations. The script uses ParaView’s `pvpython` interface.
- **Python3**: Required for running the Python scripts.
  

## Instructions

### Step 1: Setting Up the Simulation
The Python script `test_simulation_setup.py` handles the configuration of initial and boundary conditions, momentum transport models, physical properties, and control parameters for the Backward Facing Step simulation. This script is designed to copy a pre-existing template and update all necessary settings.

- **Modify Boundary Conditions**: The Python script updates initial boundary conditions like velocity (`U`), pressure (`p`), turbulent energy (`k`), and other parameters critical for running the simulation.

### Step 2: Running the Simulation (Automated with `simulate.sh`)

1. Open a terminal and navigate to the project directory.

2. Run the Bash script to automate the simulation setup and execution:
   ```bash
   ./simulate.sh
   ```

### Step 3: Viewing Results
After the simulation is complete, visualization files will be generated by ParaView. You can modify the `state.py` script for custom visualizations.

## Customization

1. **Adjusting Simulation Parameters**:  
   The simulation parameters like boundary conditions, turbulence models, viscosity, and control parameters can be adjusted directly in the `test_simulation_setup.py` script. This provides flexibility to test various physical conditions.

2. **Modifying the Template Directory**:  
   The `backwardFacingStep_template/` directory contains the base configuration files for the simulation. You can modify the mesh or turbulence models directly in this directory if needed.

### Example Commands
Here are a few examples of modifying the simulation setup:
- To change the turbulence model to `kOmegaSST`:
  ```python
  rs.update_momentumTransport(model="kOmegaSST")
  ```
- To update the velocity boundary condition at the inlet:
  ```python
  rs.update_initial_boundary_values("U", "(0 0 0)", "(44.2 0 0)")
  ```

## Conclusion

This project streamlines the process of running OpenFOAM simulations by automating the setup, execution, and post-processing steps using Python and Bash scripts.
