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


def valid_new_pokemon_schema(dictionary):
    val = validator.Validator(_NEW_POKEMON_SCHEMA)
    return val.validate(dictionary)


def valid_pokemon_dict_to_id_body(dictionary):
    pokemon_id = dictionary.get('pokadex_id')
    return int(pokemon_id), dictionary

