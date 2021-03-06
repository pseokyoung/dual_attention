import os
import shutil
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from tensorflow import keras
 
def checkgpu():
    from tensorflow.python.client import device_lib
    
    print(device_lib.list_local_devices())
    
def createfolder(path):
    if not os.path.exists(path):#
        os.makedirs(path)
        
def removefolder(path):
    shutil.rmtree(path, ignore_errors=True)
        
def loadfile(file_path, file_name, file_type='csv', header=0, print_msg=True):
    if file_type == 'csv':
        file_load = pd.read_csv(f"{file_path}/{file_name}.csv", header=header)
        if print_msg:
            print(f"csv file is loaded from {file_path}/{file_name}.csv")
        
    elif file_type == 'pkl':
        file_load = joblib.load(f"{file_path}/{file_name}.pkl")
        if print_msg:
            print(f"pkl file is loaded from: {file_path}/{file_name}.pkl")

    elif file_type == 'model':
        file_load = keras.models.load_model(f"{file_path}/{file_name}")
        if print_msg:
            print(f"model is loaded from: {file_path}/{file_name}")
                
    return file_load

def savefile(file_save, file_path, file_name, file_type='csv', index=False):
    createfolder(file_path)
    if file_type == 'csv':
        file_save.to_csv(f"{file_path}/{file_name}.csv", index = index)
        print(f"csv file is saved to: {file_path}/{file_name}.csv")

    elif file_type == 'pkl':
        joblib.dump(file_save, f"{file_path}/{file_name}.pkl")
        print(f"pkl is saved to: {file_path}/{file_name}.pkl")   
         
    elif file_type == 'figure':
        plt.savefig(f"{file_path}/{file_name}.png")

def exists(file_path):
    istrue = os.path.exists(f"{file_path}")
    return istrue