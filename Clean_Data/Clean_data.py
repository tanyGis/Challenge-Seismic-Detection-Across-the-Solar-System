import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

def find_files(extension):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    pattern = os.path.join(current_directory, f'**/*.{extension}')
    matches = glob.glob(pattern, recursive=True)
    
    return [os.path.splitext(os.path.basename(file))[0] for file in matches]

name_list = find_files('csv')

for value in name_list:
    #Read CSV and convert to DataFrame
    data = pd.read_csv(value + '.csv')
    
    #Get Velocity data
    velocity = data.loc[:, 'velocity(c/s)']
    
    #Split between positive and negative, assign limits
    pos_velocity = velocity[velocity>0]
    neg_velocity = velocity[velocity<0]
    
    pos_velocity_mean = pos_velocity.mean()
    neg_velocity_mean = neg_velocity.mean()
    
    pos_velocity_std = pos_velocity.std()
    neg_velocity_std = neg_velocity.std()
    
    uppr_lim = pos_velocity_mean + pos_velocity_std
    lowr_lim = neg_velocity_mean - neg_velocity_std
    
    #Plotting
    csv_times = np.array(data['rel_time(sec)'].tolist())
    csv_data = np.array(data['velocity(c/s)'].tolist())
    
    fig,ax = plt.subplots(1,1,figsize=(10,3))
    ax.plot(csv_times,csv_data)

    ax.set_xlim([min(csv_times),max(csv_times)])
    ax.set_ylabel('Velocity (c/s)')
    ax.set_xlabel('Time (s)')
    ax.set_title(f'{value}', fontweight='bold')
    
    #Plot limit lines before cleaning
    pos_mean = ax.axhline(y=uppr_lim, c='red')
    neg_mean = ax.axhline(y=lowr_lim, c='red')
    
    #Cleaning
    to_drop = []
    for vel in data['velocity(c/s)']:
        if (lowr_lim <= vel):
            if (vel <= uppr_lim):
                index = data[data['velocity(c/s)'] == vel].index
                to_drop.extend(index)
    print((len(to_drop)/len(data))*100)
    data.drop(to_drop, inplace = True)

    #Export to new CSV
    data.to_csv(value + '_clean.csv', index = False)