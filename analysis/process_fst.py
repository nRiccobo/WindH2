# Python modules
import yaml, os
import sys 
import shutil
import numpy as np
import pandas as pd

# Instantiate fast_IO
from ROSCO_toolbox.ofTools.fast_io import output_processing
from ROSCO_toolbox.inputs.validation import load_rosco_yaml
from datetime import datetime

# WHAT? User inputs
project_name = 'baseline_' + '20230204' #datetime.today().strftime('%Y%m%d')

sys.path.insert(0, '../src')
import utilities as util

# WHO? initiate root and current directories 
this_dir = os.getcwd()
root_dir = os.path.join(this_dir, os.pardir)

# WHAT? specify input files for turbine selection
input_dir = os.path.join(root_dir, 'inputs')
input_file = 'NREL3p4MW.yaml' # IEA15MW.yaml or IEA3p4MW.yaml 
output_dir = os.path.join(root_dir, 'results', project_name)
figure_dir = os.path.join(output_dir, 'figures')


inps = load_rosco_yaml(os.path.join(input_dir, input_file))
path_params         = inps['path_params']

# WHERE? specify OpenFast directory for output files
fast_dir = os.path.join(root_dir, path_params['FAST_directory']) 
fast_file = path_params['FAST_InputFile']

#out_files = ['weis_job_0_derated.outb', 'weis_job_0.outb']
out_files = util.list_of_files(output_dir, '.outb')

out_filepaths = [os.path.join(output_dir,out) for out in out_files]
print(out_filepaths)
# Define Plot cases: How? 
cases = {}
cases['Rot. Speed Sigs.'] = ['Wind1VelX', 'RotTorq', 'RotSpeed', 'RotThrust']
cases['Gen. Speed Sigs.'] = ['RtVAvgxh', 'GenTq', 'GenSpeed', 'GenPwr']
cases['IPC. Control Sigs.'] = ['RtTSR', 'BldPitch1','BldPitch2', 'BldPitch3']
cases['Yaw Sigs.'] = ['NacYaw', 'YawBrFxp', 'YawBrFyp','YawBrFzp']

op = output_processing.output_processing()
fast_out = []
fast_out = op.load_fast_out(out_filepaths, tmin=0)

i_fig = 1
fig, ax = op.plot_fast_out(fast_out, cases, showplot=True)
save_fig_dir = '.'
for f in fig:
    f.savefig(os.path.join(save_fig_dir,project_name + str(i_fig)))
    i_fig += 1
#print(fast_out)
