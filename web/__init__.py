import os

from flask import Flask, render_template, url_for, redirect, request, session, send_file

from web.backend.Character import Character
from web.backend.Episode import Episode
from web.backend.Location import Location

def start_app():
    app = Flask(__name__, static_folder='static')
    app.secret_key='estoesunaclavesupersecreta'

    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')

    return app