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
        return render_template('characters.html', characters=characters, page=page)
    
    @app.route('/character/<id>', methods=['GET'])
    def character(id):
        character = Character.getById(id)
        name = Character.name(character)
        status = Character.status(character)
        species = Character.species(character)
        type = Character.type(character)
        gender = Character.gender(character)
        origin = Character.origin(character)
        location = Character.location(character)
        image = Character.image(character)
        episodes = Episode.getByList(Character.episode(character))
        return render_template('character.html', id=id, name=name, status=status, species=species, type=type,
                               gender=gender, origin=origin, location=location, image=image, episodes=episodes)
    
    # ---------------------------------- MODULO EPISODIOS
    @app.route('/episodes', methods=['GET'])
    def episodes():
        numEpisodes = Episode.count(Episode.info(Episode.get_all()))
        listIdEpisodes = [i for i in range(1, numEpisodes + 1)]
        episodes = Episode.getByList(listIdEpisodes)
        seasons = Episode.getEpisodes(episodes)
        return render_template('episodes.html', seasons=seasons)
    
    @app.route('/episode/<id>', methods=['GET'])
    def episode(id):
        episode = Episode.getById(id)
        name = Episode.name(episode)
        air_date = Episode.air_date(episode)
        episode_code = Episode.getEpisode(episode)        
        characters = Episode.characters(episode)
        return render_template('episode.html', id=id, name=name, air_date=air_date, episode_code=episode_code, characters=characters)

    # ---------------------------------- MODULO LOCALIZACIONES
    @app.route('/locations', methods=['GET'])
    def locations():
        page = request.args.get('page', default=1, type=int)
        locations = Location.results(Location.getAllPaged(page))
        graph = Location.createGraph(locations)
        imageLocations = Location.createImage(graph)
        nodesLinked = Location.nodesLinked(graph)

        return render_template('locations.html', imageLocations=imageLocations, nodesLinked=nodesLinked, 
                               locations=locations, page=page)

    # ---------------------------------- MODULO DOCS
    @app.route('/docs', methods=['GET'])
    def docs():
        return render_template('docs.html')
    
    # ---------------------------------- MODULO ABOUT
    @app.route('/about', methods=['GET'])
    def about():
        return render_template('about.html')
    
    return app