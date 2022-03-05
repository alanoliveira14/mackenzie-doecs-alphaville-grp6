import pandas as pd
import os
import json

def avg_single_car_make(id_file,car_make):

    param = car_make

    target = os.getcwd() + '/uploadedFiles/' + id_file + ".csv"

    if os.path.isfile(target) :

        df = pd.read_csv(target)

        groupby_avg = df.groupby(['car_make']).median()

        avg_value_car_make = groupby_avg['car_value']

        print(avg_value_car_make)
        print(avg_value_car_make[param])

        result = 'The Avarage of car_make: ' + str(param) + ', is: ' + str(avg_value_car_make[param])
    else:
        result = 'Arquivo não existe'

    response = result

    return response