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

        print(avg_value_city)
        print(avg_value_city[param])

        result = 'The Avarage of city: ' + str(param) + ', is: ' + str(avg_value_city[param])
    else:
        result = 'Arquivo não existe'

    response = result

    return response