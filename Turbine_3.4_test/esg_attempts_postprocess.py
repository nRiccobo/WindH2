
# Python modules
import yaml, os 
import shutil
import numpy as np
import pandas as pd
# ROSCO toolbox modules 
# from ROSCO_toolbox import turbine as ROSCO_turbine
# from ROSCO_toolbox.utilities import write_rotor_performance
# from ROSCO_toolbox.inputs.validation import load_rosco_yaml

file_dir='/Users/egrant/Desktop/WEIS_Things/WEIS/openfast_runs/WEIS_Job_ESG/Outputs/'
winds=np.arange(3,22,1)
dt=0.01
use_time=100/dt
cols=['Wind1VelX','RtAeroCp']
windspd=5
mywind=[]
myCt=[]
for windspd in winds:
  filename='weis_job_0_model_U{}.out'.format(windspd)
  data=pd.read_csv(file_dir + filename,sep='\t',skiprows=5,usecols=cols)
  start_idx=float(len(data['Wind1VelX'])-use_time)
  start_idx=round(start_idx)
  mean_wind=np.mean(data['Wind1VelX'][start_idx:-1])
  mean_ct=np.mean(data['RtAeroCp'][start_idx:-1])
  mywind.append(mean_wind)
  myCt.append(mean_ct)
[]
# cp_table=pd.DataFrame([mywind,myCt])
# cp_table=cp_table.T
# cp_table.columns=['Wind','RtAeroCp']
# cp_table.to_csv(file_dir + 'Cp_Curve_Data.csv')
