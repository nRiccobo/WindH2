
# Python modules
import yaml, os 
import shutil
import numpy as np
# ROSCO toolbox modules 
# from ROSCO_toolbox import turbine as ROSCO_turbine
# from ROSCO_toolbox.utilities import write_rotor_performance
# from ROSCO_toolbox.inputs.validation import load_rosco_yaml
exe_dir='/Users/egrant/Desktop/WEIS_Things/WEIS/local/bin/openfast'
file_dir='/Users/egrant/Desktop/WEIS_Things/WEIS/openfast_runs/WEIS_Job_ESG/'
winds=np.arange(3,26,1)
os.chdir(file_dir)
for windspd in winds:
#windspd=5
  new_iflow='weis_job_0_InflowFile_U{}.dat'.format(windspd)
  shutil.copyfile(file_dir + 'weis_job_0_InflowFile.dat',file_dir+new_iflow)
  new_fst='weis_job_0_model_U{}.fst'.format(windspd)
  shutil.copyfile(file_dir + 'weis_job_0.fst',file_dir+new_fst)
  # with open (file_dir + new_iflow,"a+") as iflow_w:
  with open(file_dir + 'weis_job_0_InflowFile.dat','r') as iflw_r:
    og_iflw=iflw_r.readlines()
  []
  with open (file_dir + 'weis_job_0.fst','r') as fst_r:
    og_fst=fst_r.readlines()
  old_str=og_iflw[12]
  newstr=old_str
  old_str_fst=og_fst[36]
  newstr_fst=old_str_fst
  idx_end=old_str_fst.find('" InflowFile')
  newstr_fst=newstr_fst.replace(newstr_fst[0:idx_end+1],'"' + new_iflow+'"')
  #newstr[0:2]=str(windspd)
  newstr=newstr.replace(newstr[0],str(windspd))
  fst_handle=open(file_dir + 'weis_job_0.fst','r')
  fst_content=fst_handle.read()
  fst_content=fst_content.replace(old_str_fst,newstr_fst)
  fst_handle.close()
  fst_w=open(file_dir + new_fst,"w")
  fst_w.write(fst_content)
  fst_w.close()
  inflow_handle=open(file_dir + 'weis_job_0_InflowFile.dat','r')
  content=inflow_handle.read()
  content=content.replace(old_str,newstr)
  inflow_handle.close()
  iflow_w=open(file_dir + new_iflow,"w")
  iflow_w.write(content)
  iflow_w.close()
  iflw_r.close()
  fst_r.close()
  []
  cmd=exe_dir + ' ' + new_fst
  os.system(cmd)
  shutil.move(file_dir+'weis_job_0_model_U{}.out'.format(windspd),file_dir + "Outputs/"+'weis_job_0_model_U{}.out'.format(windspd))
  print("Done with {} m/s".format(windspd))
  []
[]
#fst_file=
