import pandas as pd
import os
import json

def avg_single_city(id_file,city):

    param = city

    target = os.getcwd() + '/uploadedFiles/' + id_file + ".csv"

    if os.path.isfile(target) :

        df = pd.read_csv(target)

        groupby_avg = df.groupby(['city']).median()

        avg_value_city = groupby_avg['car_value']

        transform_json = avg_value_city.to_json(orient="table")
        parsed = json.loads(transform_json)
        transform_json = json.dumps(parsed, indent=4)

        response = transform_json
    else:
        response = 'Arquivo não existe'

    return response