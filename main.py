from flask import Flask, make_response, jsonify, request
from bd import Summaries
import random

##instancia o flask da aplicação
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/get_weather', methods=['GET'])
#marca como rota, e define seu verbo http;
def get_weather():
    return make_response(
        jsonify(
            Summaries = random.choice(Summaries),
            temperature = random.randint(-20, 55)
        )   
    )

@app.route('/create_weather', methods=['POST'])
def create_weather():
    weather = request.json
    Summaries.append(weather)
    return make_response(
        jsonify(
                mensagem = 'Summarie successfully created.',
                summarie = weather
            )
    )

@app.route('/remove_weather', methods=['DELETE'])
def remove_weather():
    weather = request.json
    Summaries.remove(weather)
    return make_response(
        jsonify(
            mensagem = 'Summarie sucessfully deleted.',
            Summaries = Summaries
        )
    )

app.run()

