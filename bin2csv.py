import os
import numpy as np
import pandas as pd

# MAKE PATH
def make_path(path):
    try:
        os.makedirs(path)
    except:
        pass

# MAKE LIST TO ARRAY
def list2array(columns):
    for col in columns:
        col = np.array(col).reshape(-1, )
        print(col)
        print(len(col))
    
    return columns

# MAKE ARRAY TO TRANSPOSE
def array2array_t(columns):
    data = np.array(columns)
    data = data.T
    
    return data

# MAKE ARRAY TO DATAFRAME
def array_t2dataframe(data, features):
    df = pd.DataFrame(data = data,
                      columns = features)
    
    return df

def main():

    magic, seq, pressure = [], [], []
    pos_cmd, pos_fdb, loadcell = [], [], []
    t1, t2, t3, t4, t5 = [], [], [], [], []
    ls_max, ls_min, x_acc, y_acc, z_acc = [], [], [], [], []
    rms_acc, rms_vel, rms_pos = [], [], []
    temp, humid, sound_level, dev_err = [], [], [], []
    micsel, miclvl = [], []

    # [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    columns = [
                seq, pressure,
                pos_cmd, pos_fdb, loadcell,
                t1, t2, t3, t4, t5,
                ls_max, ls_min, x_acc, y_acc, z_acc,
                rms_acc, rms_vel, rms_pos,
                temp, humid, sound_level, dev_err,
                micsel, miclvl
              ]

    # 
    features = [
                'seq', 'pressure',
                'pos_cmd', 'pos_fdb', 'loadcell',
                't1', 't2', 't3', 't4', 't5',
                'ls_max', 'ls_min', 'x_acc', 'y_acc', 'z_acc',
                'rms_acc', 'rms_vel', 'rms_pos',
                'temp', 'humid', 'sound_level', 'dev_err',
                'micsel', 'miclvl'
               ]

    data = './data/data2.bin'

    with open(data, 'r', errors='ignore') as f:
        for _ in range(11837):
            magic.append(np.fromfile(f, 'u2', 2))        # uint32
            seq.append(np.fromfile(f, 'u2', 1))          # uint16
            pressure.append(np.fromfile(f, 'u1', 1))     # uint8
            pos_cmd.append(np.fromfile(f, 'u1', 1))      # uint8
            pos_fdb.append(np.fromfile(f, 'u1', 1))      # uint8
            loadcell.append(np.fromfile(f, 'i2', 1))     # int16
            t1.append(np.fromfile(f, 'i2', 1))           # int16
            t2.append(np.fromfile(f, 'i2', 1))           # int16
            t3.append(np.fromfile(f, 'i2', 1))           # int16
            t4.append(np.fromfile(f, 'i2', 1))           # int16
            t5.append(np.fromfile(f, 'i2', 1))           # int16
            ls_max.append(np.fromfile(f, 'u1', 1))       # uint8   
            ls_min.append(np.fromfile(f, 'u1', 1))       # uint8
            x_acc.append(np.fromfile(f, 'i2', 1))        # int16
            y_acc.append(np.fromfile(f, 'i2', 1))        # int16
            z_acc.append(np.fromfile(f, 'i2', 1))        # int16
            rms_acc.append(np.fromfile(f, 'i2', 1))      # int16
            rms_vel.append(np.fromfile(f, 'i2', 1))      # int16
            rms_pos.append(np.fromfile(f, 'i2', 1))      # int16
            temp.append(np.fromfile(f, 'i1', 1))         # int8
            humid.append(np.fromfile(f, 'u1', 1))        # uint8
            sound_level.append(np.fromfile(f, 'u2', 1))  # uint16
            dev_err.append(np.fromfile(f, 'u2', 1))      # uint16
            micsel.append(np.fromfile(f, 'u1', 1))       # uint8
            miclvl.append(np.fromfile(f, 'u2', 1))       # uint16
    
    columns = list2array(columns)
    
    data = array2array_t(columns)
    data = data.reshape(-1, 24)

    df = array_t2dataframe(data, features)

    make_path(path='results')
    df.to_csv('./results/result.csv', index=False)
    

if __name__ == '__main__':

    main()