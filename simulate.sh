#!/bin/bash

# Set the name of the simulation directory and the Python script used for setup
SIM_DIR="TestBackwardFacingStep"
SIMULATION_SETUP_SCRIPT="test_simulation_setup.py"

# Run the Python script to configure the simulation with the necessary boundary conditions and parameters
python3 $SIMULATION_SETUP_SCRIPT $SIM_DIR

# Change directory to the simulation folder
cd $SIM_DIR

# Generate the computational mesh using the blockMesh utility in OpenFOAM
echo "Generating Block Mesh..."
blockMesh

# Run the CFD simulation using the SIMPLE algorithm via simpleFoam in OpenFOAM
echo "Running SIMPLE FOAM Simulation..."
simpleFoam

# Generate post-processing visualization using ParaView's Python scripting interface
echo "Generating Visualization..."
pvpython --force-offscreen-rendering state.py

# Return to the parent directory after the simulation is complete
cd ..

echo "Simulation Complete"
