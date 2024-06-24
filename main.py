"""
A&G

Implémentation de ALGO1
"""
import pandas as pd

# File paths
txt_file_path = 'data1.txt'

# Reading the text file
with open(txt_file_path, 'r') as file:
    lines = file.readlines()

# Extracting general information
nbLocalisations = int(lines[0].split()[1])
nbRessources = int(lines[1].split()[1])
nbMachines = int(lines[2].split()[1])
nbProcessus = int(lines[3].split()[1])
nbServices = int(lines[4].split()[1])

# Extracting Machines data
machines_start = lines.index('*******Machines*******\n') + 1
machines_end = lines.index('*******Services*******\n')

machines_data = []
for line in lines[machines_start:machines_end]:
    machines_data.append([int(x) for x in line.split()])

# Extracting Services data
services_start = machines_end + 1
services_end = lines.index('*******Processus*******\n')

services_data = []
for line in lines[services_start:services_end]:
    services_data.append(int(line.strip()))

# Extracting Processus data
processus_start = services_end + 1

processus_data = []
for line in lines[processus_start:]:
    processus_data.append([int(x) for x in line.split()])

# Creating DataFrames
machines_df = pd.DataFrame(machines_data, columns=['Localisation'] + [f'Resource_{i}' for i in range(nbRessources)])
services_df = pd.DataFrame(services_data, columns=['Service'])
processus_df = pd.DataFrame(processus_data, columns=['Service'] + [f'Resource_{i}' for i in range(nbRessources)])

# Display DataFrames
import ace_tools as tools; tools.display_dataframe_to_user(name="Machines Data", dataframe=machines_df)
tools.display_dataframe_to_user(name="Services Data", dataframe=services_df)
tools.display_dataframe_to_user(name="Processus Data", dataframe=processus_df)
