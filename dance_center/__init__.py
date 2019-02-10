import os
from flask import Flask, url_for
from flask_restful import Api

dance_center_app = Flask(__name__)
dance_center_app.config.from_object(os.environ.get('app_env'))
api = Api(dance_center_app, prefix='/v1')

from dance_center.dance_center_main import DanceCenter

dance_center_main = DanceCenter.as_view(name='dance_center_main')
dance_center_app.add_url_rule('/', view_func=dance_center_main, methods=['GET'])
