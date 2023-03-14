# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:41:53 2023

@author: RM67UE
"""

import os
import requests



AZURE_DEVOPS_PAT = "Put your PAT here"
url = 'https://dev.azure.com/negisandip7/P012345/_apis/wit/workitems/$task?api-version=5.1'
project = 'P012345'
current_sprint = 'Sprint 1'
itr_path = "{}\{}".format(project,current_sprint)
input_file = "C:\\Users\RM67UE\OneDrive - ING\Desktop\stage_monitoring\sandeep\stg6to5\POC\Expiring_controls_14_days.csv"
with open(input_file) as inp:
    for line in inp.readlines()[1:]:
        print(line)
        asset =line.split(',')[0]
        control=line.split(',')[1]
        exp_date = line.split(',')[2]

        document_patch = []
        default_fields={
            'System.State':'To do',
            'System.IterationPath': itr_path,
            'System.Title' : "{} for {} expiring on {}".format(control,asset,exp_date),
            'System.Description' : 'Take necessary action'
    
            }

        for field in default_fields:
            document_patch.append(
                {
                    "op":"add",
                    "path":"/fields/"+field,
                    "value":default_fields[field]
                    }
        
                )
    

        r = requests.post(url, json=document_patch, 
                      headers={'Content-Type': 'application/json-patch+json'},
                      auth=('', AZURE_DEVOPS_PAT))

        print(r.json())