import pandas as pd
import os
import json

def avg_city(id_file):
   
    target = os.getcwd() + '/uploadedFiles/' + id_file + ".csv"

    if os.path.isfile(target):

        df = pd.read_csv(target)
        groupby_avg = df.groupby(['city']).median()

        avg_value_car_make = groupby_avg['car_value']

        transform_json = avg_value_car_make.to_json(orient="table")
        parsed = json.loads(transform_json)
        transform_json = json.dumps(parsed, indent=4)

        response = transform_json
    else:
        response = 'Arquivo não existe'

    return response