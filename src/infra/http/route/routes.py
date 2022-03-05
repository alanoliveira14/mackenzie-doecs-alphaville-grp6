from flask import jsonify, request
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.arquivoController as arquivoController
import src.controller.avg_car_make as avg_car_make
import src.controller.avg_single_car_make as avg_single_car_make
import src.controller.avg_city as avg_city
import src.controller.avg_single_city as avg_single_city
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

    @app.route('/avgsiglecarmake/<id_file>/carmake/<car_make>', methods=['GET'])
    @auth.requires_auth
    def request_get_avg_single_car_make(id_file,car_make):
        try:
            response = avg_single_car_make.avg_single_car_make(id_file,car_make)

            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500

    @app.route('/avgcity/<id_file>', methods=['GET'])
    @auth.requires_auth
    def request_get_avg_city(id_file):
        try:
            response = avg_city.avg_city(id_file)

            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500

    @app.route('/avgsiglecity/<id_file>/city/<city>', methods=['GET'])
    @auth.requires_auth
    def request_get_avg_single_city(id_file,city):
        try:
            response = avg_single_city.avg_single_city(id_file,city)

            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500
