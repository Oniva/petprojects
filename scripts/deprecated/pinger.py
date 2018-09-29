#! python 3
#  checks if certain ip's ping from a json


import json, os, subprocess


dir = "#"

with open(dir, "r") as f:
    data = json.load(f)

for comp in data:

    currentIP = data['{}'.format(comp)]['ip']

    try:
        result = str(subprocess.check_output('ping -c 1 {}'.format(currentIP), shell=True))
        
        if '1 packets received' in result:
            data['{}'.format(comp)]['up'] = 'True'
            
            with open(dir, "w") as f:
                json.dump(data, f)     

    except subprocess.CalledProcessError:
        data[comp]['up'] = 'False'

        with open(dir, "w") as f:
            json.dump(data, f)


   
