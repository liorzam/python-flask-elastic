from run import app, es
from flask import request, jsonify
import flaskr.utils as utils

POKEMON_INDEX = 'pokemon'

@app.route('/', methods=['GET'])
def index():
    return 'This is the index page\n'


@app.route('/new_pokemon', methods=['POST'])
def add_pokemon():
    if not utils.valid_new_pokemon_schema(request.json):
        return 'Bad Request\n'
    pokemon_id, pokemon_body = utils.valid_pokemon_dict_to_id_body(request.json)
    result = es.index(index=POKEMON_INDEX, id=pokemon_id, body=pokemon_body)
    return f'New Pokemon Added\n{jsonify(result)}\n'


@app.route('/autocomplete/<string:pokemon>')
def auto_complete(pokemon):
    fields = ['nickname', 'name', 'skills']
    results = es.search(index=POKEMON_INDEX,
                        body={'query': {'multi_match': {'fields': fields, 'query': pokemon, }}})
    return jsonify(results['hits']['hits'])


@app.route('/query_pokemon', methods=['POST'])
def query():
    results = es.get(index=POKEMON_INDEX, id=int(request.json.get('id', 0)))
    return jsonify(results['_source'])
