
# Python modules
import yaml, os 
import shutil
import numpy as np
import random
# ROSCO toolbox modules 
# from ROSCO_toolbox import turbine as ROSCO_turbine
# from ROSCO_toolbox.utilities import write_rotor_performance
# from ROSCO_toolbox.inputs.validation import load_rosco_yaml
# def run_turbsim(exe_dir,turbsim_filedir,turbsim_template_filename,mean_windspeed,analysis_time_sec,generate_new_seed=False,random_num=1501552846):
#   []
file_dir= os.path.abspath('')

weis_main_path = '/Users/egrant/Desktop/WEIS_Things/WEIS/'
exe_dir=weis_main_path + 'local/bin/'
# exe_dir='/Users/egrant/Desktop/WEIS_Things/WEIS/local/bin/openfast'
# file_dir='/Users/egrant/Desktop/WEIS_Things/WEIS/openfast_runs/WEIS_Job_ESG/'
file_dir='/Users/egrant/Desktop/WEIS_Things/WEIS/openfast_runs/AutoTurb/'
openfast_filedir='/Users/egrant/Desktop/WEIS_Things/WEIS/openfast_runs/WEIS_Job_ESG/'
turbsim_filedir=weis_main_path + 'openfast_runs/wind/'

turbsim_output_dir = weis_main_path + 'openfast_runs/wind/'
openfast_inputfiledir = weis_main_path + 'OpenFAST_Files/'
openfast_outputdir = weis_main_path + 'Results/'
# template_dir = weis_main_path + 'AutoTurb/'
template_dir = file_dir #weis_main_path + 'AutoTurb/'

turbsim_template_filename = 'turbsim_template.in'
inflow_template_filename = 'inflow_template.dat'
model_template_filename = 'model_template.fst'

run_turbsim=True
# turbsim_params = ['RandSeed1','AnalysisTime','HubHt','URef']
# turbsim_vals = ['1501552846','700','120',str(windspd)]
# turbsim_dict = dict(zip(turbsim_params,turbsim_vals))
inflow_params = ['WindType','FileName_BTS']
model_params = ['TMax','InflowFile']
# winds=np.arange(3,26,1)
winds=np.arange(8,10,1)
os.chdir(file_dir)
for windspd in winds:
  randseed=12345678#1501552846
  tb_time = 708
  huht= 120 #DOUBLE CHECK
  turbsim_params = [' RandSeed1 ',' AnalysisTime ',' HubHt ',' URef ']
  turbsim_vals = [str(randseed),str(tb_time),str(huht),str(windspd)]
  turbsim_dict = dict(zip(turbsim_params,turbsim_vals))

  turb_ipt_newname='TurbSim_U{}_Seed{}_Time{}.in'.format(windspd,randseed,tb_time) 
  shutil.copyfile(template_dir  + turbsim_template_filename,turbsim_output_dir+turb_ipt_newname)
  turb_handle=open(template_dir  + turbsim_template_filename,'r')
  turb_content=turb_handle.read()
  with open(template_dir  + turbsim_template_filename,'r') as read_turb:
    turb_lines=read_turb.readlines()
  for tbi,tb_param in enumerate(turbsim_params):
    tb_lineIdx=[line_i for line_i,line in enumerate(turb_lines) if tb_param in line]
    tb_line=[line for line in turb_lines if tb_param in line]
    tb_newline = tb_line[0]
    # idx_end = tb_line[0].find(' ' + tb_param)
    idx_end = tb_line[0].find(' ')
    tb_newline=tb_newline.replace(tb_newline[0:idx_end+1],turbsim_vals[tbi])
    turb_content=turb_content.replace(tb_line[0],tb_newline)

  
  # turb_content=turb_content.replace(old_str,newstr)
  turb_handle.close()
  turb_write=open(turbsim_output_dir+turb_ipt_newname,"w")
  turb_write.write(turb_content)
  turb_write.close()
  read_turb.close()

  if run_turbsim:
    cmd = exe_dir + 'turbsim ' + turbsim_output_dir + turb_ipt_newname
    os.system(cmd)
    # shutil.move(file_dir+'TurbSim_U{}_Seed{}_Time{}.bts'.format(windspd,randseed,tb_time) ,turbsim_output_dir  +'TurbSim_U{}_Seed{}_Time{}.bts'.format(windspd,randseed,tb_time) )
    []


  


#   new_iflow='InflowFile_U{}.dat'.format(windspd)
#   shutil.copyfile(template_dir  + inflow_template_filename,openfast_inputfiledir+new_iflow)
#   new_fst='weis_job_0_model_U{}.fst'.format(windspd)
#   shutil.copyfile(file_dir + 'weis_job_0.fst',file_dir+new_fst)
#   # with open (file_dir + new_iflow,"a+") as iflow_w:
#   with open(file_dir + 'weis_job_0_InflowFile.dat','r') as iflw_r:
#     og_iflw=iflw_r.readlines()
#   []
#   with open (file_dir + 'weis_job_0.fst','r') as fst_r:
#     og_fst=fst_r.readlines()
#   old_str=og_iflw[12]
#   newstr=old_str
#   old_str_fst=og_fst[36]
#   newstr_fst=old_str_fst
#   idx_end=old_str_fst.find('" InflowFile')
#   newstr_fst=newstr_fst.replace(newstr_fst[0:idx_end+1],'"' + new_iflow+'"')
#   #newstr[0:2]=str(windspd)
#   newstr=newstr.replace(newstr[0],str(windspd))
#   fst_handle=open(file_dir + 'weis_job_0.fst','r')
#   fst_content=fst_handle.read()
#   fst_content=fst_content.replace(old_str_fst,newstr_fst)
#   fst_handle.close()
#   fst_w=open(file_dir + new_fst,"w")
#   fst_w.write(fst_content)
#   fst_w.close()

#   inflow_handle=open(file_dir + 'weis_job_0_InflowFile.dat','r')
#   content=inflow_handle.read()
#   content=content.replace(old_str,newstr)
#   inflow_handle.close()
#   iflow_w=open(file_dir + new_iflow,"w")
#   iflow_w.write(content)
#   iflow_w.close()
#   iflw_r.close()
#   fst_r.close()
#   []
#   cmd=exe_dir + ' ' + new_fst
#   os.system(cmd)
#   shutil.move(file_dir+'weis_job_0_model_U{}.out'.format(windspd),file_dir + "Outputs/"+'weis_job_0_model_U{}.out'.format(windspd))
#   print("Done with {} m/s".format(windspd))
#   []
# []
# #fst_file=
