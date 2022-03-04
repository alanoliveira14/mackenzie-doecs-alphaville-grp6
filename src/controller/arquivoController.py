import os
import uuid
import json
from builtins import print


def receiveFile(arquivo):

    print('iniciando salvamento do arquivo')

    nomeUnicoArquivo = str(uuid.uuid1())

    arquivo.save(os.path.join("uploadedFiles/", nomeUnicoArquivo))

    response = {
        "idArquivo": nomeUnicoArquivo,
        "arquivoEnviado":arquivo.filename
    }

    if os.path.isfile('auxiliar/arquivosEnviados.json'):
        try:
            with open('auxiliar/arquivosEnviados.json') as json_file:
                data = json.load(json_file)
                data["arquivos"].append(response)
                print("incrementando json de registro")
                gravaArquivo(data)
        except Exception as ex:
            print(ex)
    else:
        print("criando json de registro")
        data = {'arquivos': [response]}
        gravaArquivo(data)

    print('gravação finalizada')


    return response

def gravaArquivo(data):
    with open('auxiliar/arquivosEnviados.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)