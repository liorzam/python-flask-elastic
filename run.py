import os

from elasticsearch import Elasticsearch
from flask import Flask
from configs.config import load_config

cfg = load_config(os.path.join('configs', 'app_config.yaml'))
es_cfg = cfg['ES_CONNECTION']

es = Elasticsearch([{"host": es_cfg['HOST'], "port": int(es_cfg['PORT'])}])

app = Flask(__name__)

import flaskr.routes
