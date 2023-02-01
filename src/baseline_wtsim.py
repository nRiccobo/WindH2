'''
This script runs a baseline openFAST simulation of the IEA-3.4MW Wind turbine
'''

# Load Modules
import os

from ROSCO_toolbox import controller as ROSCO_controller
from ROSCO_toolbox import turbine as ROSCO_turbine
from ROSCO_toolbox.utilities import write_DISCON, run_openfast
from ROSCO_toolbox.inputs.validation import load_rosco_yaml

# Directory: You are where?
this_dir = os.getcwd()
root_dir = os.path.join(this_dir, os.pardir)
weis_dir = os.path.join(root_dir, os.pardir, 'WEIS') # System append? or imports?
output_dir = os.path.join(root_dir,'results')
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# Load input configuration file for turbine selection
input_dir = os.path.join(root_dir, 'inputs')
input_file = 'IEA3p4MW.yaml' # IEA15MW.yaml or IEA3p4MW.yaml 

#parameter_filename = os.path.join(tune_dir,'NREL5MW.yaml')
inps = load_rosco_yaml(os.path.join(input_dir, input_file))
path_params         = inps['path_params']
#turbine_params      = inps['turbine_params']
#controller_params   = inps['controller_params']

# Specify OpenFast files
fast_dir = os.path.join(root_dir, path_params['FAST_directory']) 
fast_file = path_params['FAST_InputFile']

rotorperf_file = path_params['rotor_performance_filename']


# Instantiate turbine, controller, and file processing classes
# # Load turbine model from saved pickle
turbine         = ROSCO_turbine.Turbine
turbine         = turbine.load(os.path.join(output_dir,'IEA3p4_saved.p'))
#controller      = ROSCO_controller.Controller(controller_params)

# Load turbine data from OpenFAST and rotor performance text files
turbine.load_from_fast(fast_file, fast_dir, \
    dev_branch=True,rot_source='txt',\
      txt_filename=os.path.join(this_dir,fast_dir,rotorperf_file))

# Run OpenFAST
ofbin_path=os.path.join(weis_dir, 'local', 'bin', 'openfast')
run_openfast(fast_dir,fastcall=ofbin_path,fastfile=fast_file,chdir=True)