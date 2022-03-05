import pandas as pd
import os
import json

def avg_single_car_make(id_file,car_make):

    param = car_make

    target = os.getcwd() + '/uploadedFiles/' + id_file + ".csv"

    if os.path.isfile(target) :

        df = pd.read_csv(target)

        groupby_avg = df.groupby(['car_make']).median()

        avg_value_single_car_make = groupby_avg['car_value']

        print(avg_value_single_car_make)
        print(avg_value_single_car_make[param])

        transform_json = avg_value_single_car_make.to_json(orient="table")
        parsed = json.loads(transform_json)
        transform_json = json.dumps(parsed, indent=4)

        response = transform_json
    else:
        response = 'Arquivo não existe'

    return response