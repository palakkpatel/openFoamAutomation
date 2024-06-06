import os
from string import Template
import shutil

# Set the default simulation directory
SIM_DIR = "BackwardFacingStepSimulation"

def make_sim_dir(template_dir : str, sim_dir : str = None, overwrite=True):
    """
    Create a new simulation directory by copying from the provided template directory.
    
    Args:
    - template_dir (str): The path to the template directory to copy.
    - sim_dir (str, optional): The name of the simulation directory to create. Defaults to SIM_DIR.
    """
    global SIM_DIR
    if sim_dir is None:
        sim_dir=SIM_DIR
    else:
        SIM_DIR = sim_dir

    if os.path.isdir(sim_dir) and overwrite:
        print("Dir Exists, Replacing it")
        shutil.rmtree(sim_dir)

    shutil.copytree(template_dir, sim_dir)
    print(f"Created Simulation Dir {sim_dir}")


