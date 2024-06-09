import sys
import run_simulation as rs  # Import the module containing simulation setup functions

# Create a new simulation directory by copying from the template directory
rs.make_sim_dir(template_dir="backwardFacingStep_template", sim_dir=sys.argv[1])

# Update the initial and boundary conditions for various fields in the simulation
# These updates modify the field files in the "0/" directory

rs.update_initial_boundary_values("epsilon", 17.83)  # Update the 'epsilon' field value
rs.update_initial_boundary_values("f", 0)  # Update the 'f' field value
rs.update_initial_boundary_values("k", 1.09e-3)  # Update the 'k' (turbulent kinetic energy) field value
rs.update_initial_boundary_values("nut", 0)  # Update the 'nut' (turbulent viscosity) field value
rs.update_initial_boundary_values("nuTilda", 0)  # Update the 'nuTilda' field value
rs.update_initial_boundary_values("omega", 181753.313)  # Update the 'omega' field value
rs.update_initial_boundary_values("p", 0)  # Update the 'p' (pressure) field value

# Update the velocity 'U' field with both the internal field value and inlet boundary value
rs.update_initial_boundary_values("U", "(0 0 0)", "(44.2 0 0)")

rs.update_initial_boundary_values("v2", 0.25)  # Update the 'v2' field value

# Update the momentum transport settings in the simulation configuration
rs.update_momentumTransport(model="kOmegaSST")  # Set the turbulence model to 'kOmegaSST'

# Update the physical properties of the fluid (e.g., kinematic viscosity)
rs.update_physicalProperties(nu="1.56e-05")  # Set the kinematic viscosity 'nu'

# Update the control dictionary (system/controlDict) with the end time and other control parameters
rs.update_controlDict(endTime=2000)  # Set the simulation end time to 2000 seconds
