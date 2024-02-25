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

    # ---------------------------------- MODULO PERSONAJES
    @app.route('/characters', methods=['GET'])
    def characters():
        page = request.args.get('page', default=1, type=int)
        characters = Character.results(Character.getAllPaged(page))
        info = Character.info(Character.getAllPaged(page))
        return render_template('characters.html', characters=characters, info=info, page=page)
    
    # ---------------------------------- MODULO EPISODIOS
    @app.route('/episodes', methods=['GET'])
    def episodes():
        numEpisodes = Episode.count(Episode.info(Episode.get_all()))
        listaIdEpisodes = [i for i in range(1, numEpisodes + 1)]
        episodes = Episode.getByList(listaIdEpisodes)
        seasons = Episode.getEpisodes(episodes)
        return render_template('episodes.html', seasons=seasons)
    
    # ---------------------------------- MODULO LOCALIZACIONES
    @app.route('/locations', methods=['GET'])
    def locations():
        return render_template('locations.html')

    # ---------------------------------- MODULO DOCS
    @app.route('/docs', methods=['GET'])
    def docs():
        return render_template('docs.html')
    
    # ---------------------------------- MODULO ABOUT
    @app.route('/about', methods=['GET'])
    def about():
        return render_template('about.html')
    
    return app