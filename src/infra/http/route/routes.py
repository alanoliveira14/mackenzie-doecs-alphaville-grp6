from flask import jsonify, request
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.arquivoController as arquivoController
import flask

def route(app: flask.app.Flask):
    @app.route("/inputfile", methods=['POST'])
    @auth.requires_auth
    def inputFile():
        try:

            print ("RECEBIDO ARQUIVO:")
            print (request.files.get('file'))

            response = arquivoController.receiveFile(request.files.get('file'))

            return jsonify(response) , 200
        except Exception as err:

            return Http.handle_generic_http_error(err)

        return jsonify(response) , 500