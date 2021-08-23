import numpy as np
import vtu_class as vtu
import os

def set_vtus(csv_file):
    """
    Sets the given csv file into the vtus for the 1 building simulation visualisation
    """
    
    field = np.loadtxt(csv_file)
    os.chdir("summer_project")
    i = 0
    for row in field:
        file = vtu.vtufile("cube_disp_" + str(i))
        file.setField(row)
        file.save_as("cube_disp_" + str(i))
        i += 1
        
    
    
def set_vtus3bld(csv_file):
    """
    Sets the given csv file into the vtus for the 3 buildings simulation visualisation
    """
    
    field = np.loadtxt(csv_file)
    os.chdir("3bld")
    i = 0
    for row in field:
        file = vtu.vtufile("cube_disp_3bldngs_" + str(i))
        file.setField(row)
        file.save_as("cube_disp_3bldngs_" + str(i))
        i += 1
        
        
        
def set_vtus3blddiff(csv1,csv2):
    """
    Sets the differences between the given csv files into the vtus 
    for the 3 buildings simulation visualisation
    """
    
    field1 = np.loadtxt(csv1)
    field2 = np.loadtxt(csv2)
    os.chdir("3bld")
    i = 0
    for row in field1:
        file = vtu.vtufile("cube_disp_3bldngs_" + str(i))
        file.setField(row-field2[i])
        file.save_as("cube_disp_3bldngs_" + str(i))
        i += 1
    
    
def set_vtus3bldrelatdiff(csv1,csv2):
    """
    Sets the relative differences between the given csv files into the vtus 
    for the 3 buildings simulation visualisation
    """
    
    field1 = np.loadtxt(csv1)
    field2 = np.loadtxt(csv2)
    os.chdir("3bld")
    i = 0
    for row in field1:
        file = vtu.vtufile("cube_disp_3bldngs_" + str(i))
        file.setField(abs(row-field2[i])/row)
        file.save_as("cube_disp_3bldngs_" + str(i))
        i += 1
    
    
        