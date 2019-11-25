from cerberus import validator

_VALID_POKEMON_LEVELS = [10 * x for x in range(10)]


def _valid_level(field, value, error):
    if value not in _VALID_POKEMON_LEVELS:
        error(field, "Invalid Pokemon Level")


_VALID_POKEMON_TYPES = 'ELECTRIC GROUND FIRE WATER WIND PSYCHIC GRASS'.split()


def _valid_type(field, value, error):
    if value not in _VALID_POKEMON_TYPES:
        error(field, "Invalid Pokemon Type")


_NEW_POKEMON_SCHEMA = {'pokadex_id': {'required': True, 'type': 'integer'},
                       'name': {'required': True, 'type': 'string'},
                       'nickname': {'required': True, 'type': 'string'},
                       'level': {'required': True, 'check_with': _valid_level},
                       'type': {'required': True, 'check_with': _valid_type},
                       'skills': {'required': True, 'type': 'list', 'schema': {'type': 'string'}}
                       }

_POKEMON_INDEX_SCHEMA = {
    'settings': {
     "analysis": {
          "filter": {
            "autocomplete_filter": {
              "type": "edge_ngram",
              "min_gram": 1,
              "max_gram": 20
            }
          },
          "analyzer": {
            "autocomplete": {
              "type": "custom",
              "tokenizer": "standard",
              "filter": [
                "lowercase",
                "autocomplete_filter"
              ]
            }
          }
        }
    },
    'mappings': {
        'properties': {
            'pokadex_id': {'type': 'integer'},
            'name': {'type': 'completion', 'analyzer': 'autocomplete'},
            'nickname': {'type': 'completion', 'analyzer': 'autocomplete'},
            'level': {'type': 'integer'},
            'type': {'type': 'text'},
            'skills': {'type': 'text'}
        }
    }
}


def valid_new_pokemon_schema(dictionary):
    val = validator.Validator(_NEW_POKEMON_SCHEMA)
    return val.validate(dictionary)


def valid_pokemon_dict_to_id_body(dictionary):
    pokemon_id = dictionary.get('pokadex_id')
    return int(pokemon_id), dictionary


def generate_index(elastic_obj):
    if elastic_obj.indices.exists(index='pokemon'):
        elastic_obj.indices.delete(index='pokemon')
    elastic_obj.indices.create(index='pokemon', body=_POKEMON_INDEX_SCHEMA)
