from flask import jsonify, request
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.arquivoController as arquivoController
import src.controller.avg_car_make as avg_car_make
import flask


def route(app: flask.app.Flask):
    @app.route("/inputfile", methods=['POST'])
    @auth.requires_auth
    def inputFile():
        try:

            print("RECEBIDO ARQUIVO:")
            print(request.files.get('file'))

            response = arquivoController.receiveFile(request.files.get('file'))

            return jsonify(response), 200

        except Exception as err:

            return Http.handle_generic_http_error(err)

    @app.route("/listfiles", methods=['GET'])
    @auth.requires_auth
    def listUploadedFiles():
        try:

            response = arquivoController.listaTodosArquivos()

            return jsonify(response), 200

        except Exception as ex:

            return Http.handle_generic_http_error(ex)

    @app.route('/avgcarmake/<id_file>', methods=['GET'])
    @auth.requires_auth
    def request_get_avg_fabricante(id_file):
        try:
            response = avg_car_make.avg_car_make(id_file)

            return response, 200

        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500
