import os
import uuid

def receiveFile(arquivo):

    print('iniciando salvamento do arquivo')

    nomeUnicoArquivo = str(uuid.uuid1())

    arquivo.save(os.path.join("uploadedFiles/", nomeUnicoArquivo))

    print('gravação finalizada')

    response = {
        "idArquivo": nomeUnicoArquivo,
        "arquivoEnviado":arquivo.filename
    }

    return response