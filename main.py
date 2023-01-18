from flask import Flask, make_response, jsonify, request
from bd import Summaries
import random

##instancia o flask da aplicação
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/get_carros', methods=['GET'])
#marca como rota, e define seu verbo http;
def get_weather():
    return make_response(
        jsonify(
            Summaries = random.choice(Summaries),
            temperature = random.randint(-20, 55)
        )   
    )

@app.route('/create_carro', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
                mensagem = 'Carro cadastrado com sucesso.',
                carro = carro
            )
    )

@app.route('/remove_carro', methods=['DELETE'])
def remove_carro():
    carro = request.json
    Carros.remove(carro[0])
    return make_response(
        jsonify(
            Carros
        )
    )

app.run()

