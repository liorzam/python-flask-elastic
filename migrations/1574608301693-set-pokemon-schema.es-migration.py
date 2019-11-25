from es_migration_base import BaseESMigration


class Migration(BaseESMigration):

    def __init__(self, es_object):
        super().__init__(es_object=es_object, es_index='pokemon')
        self.schema = {
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
                    'skills': {'type': 'completion', 'analyzer': 'autocomplete'}
                }
            }
        }

    def execute(self):
        if self._es_object.indices.exists(index='pokemon'):
            self._es_object.indices.delete(index='pokemon')
        self._es_object.indices.create(index='pokemon', body=self.schema)
