# Flask
from flask import render_template, redirect, request, url_for, abort, make_response
from flask.views import MethodView


# Misc
import requests
import json
import os


class DanceCenter(MethodView):
    def __init__(self):
        pass

    def get(self):
        """
        Renders Dance Center home page.
        :return: Renders the html page with all substituted content needed.
        """

        return render_template('dance_center_main.html')
