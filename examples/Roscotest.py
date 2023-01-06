'''
Based on ROSCO Example_01 and Example_02. 

In this example:
- Read .yaml input file
- Load an openfast turbine model
- Read text file with rotor performance properties
- Print some basic turbine properties
- Save the turbine as a pickle

  - Load a turbine from a saved pickle
  - Plot Cp Surface

Note: Uses the NREL 5MW
'''
import os

# ROSCO Modules
from ROSCO_toolbox import turbine as ROSCO_turbine
from ROSCO_toolbox.inputs.validation import load_rosco_yaml

import matplotlib.pyplot as plt
# ROSCO toolbox modules 
from ROSCO_toolbox import turbine as ROSCO_turbine

# Current and output Directory
cur_dir = os.path.dirname( os.path.realpath(__file__) )
out_dir = os.path.join(cur_dir,'outputs')
if not os.path.isdir(out_dir):
    os.makedirs(out_dir)

# Define ROSCO directory to load proper yaml files 
rosc_dir = os.path.join(cur_dir,'../../WEIS-fork/ROSCO')
tune_dir = os.path.join(rosc_dir,'Tune_Cases')
wt_filename = os.path.join(tune_dir,'NREL5MW.yaml')
inputs = load_rosco_yaml(wt_filename)

path_params = inputs['path_params']
turbine_params = inputs['turbine_params']

# Check if Pickled file exists 
if not os.path.exists( os.path.join(out_dir,'01_NREL5MW_saved.p') ):

    # Evaluate Turbine parameters
    turbine = ROSCO_turbine.Turbine(turbine_params)

    turbine.load_from_fast(
        path_params['FAST_InputFile'],
        os.path.join(tune_dir,path_params['FAST_directory']),
        dev_branch=True,
        rot_source='txt',txt_filename=os.path.join(tune_dir,path_params['FAST_directory'],path_params['rotor_performance_filename'])
        )

    # Print turbine info 
    print(turbine)

    # Pick the turbine model 
    turbine.save(os.path.join(out_dir,'NREL5MW_saved.p'))

else:
    print("File exists: ", os.path.join(out_dir,'01_NREL5MW_saved.p'))
    # Initialize a turbine class -- Don't need to instantiate!
    turbine = ROSCO_turbine.Turbine

    # Load quick from python pickle
    turbine = turbine.load(os.path.join(out_dir,'01_NREL5MW_saved.p'))

    # plot rotor performance 
    print('Plotting Cp data')
    turbine.Cp.plot_performance()

    if True:
        plt.savefig(os.path.join(out_dir,'02_NREL5MW_Cp.png'))
    else:
        plt.show()


