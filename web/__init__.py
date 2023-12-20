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
        return render_template('paginainicio.html')
    
    @app.route('/testBackend', methods=['GET', 'POST'])
    def testBackend(resultado=None):
        return render_template('testBackend.html', resultado=resultado)
            
    
    @app.route('/getCharacter', methods=['GET', 'POST'])
    def getCharacter():
        if request.method == 'POST':
            character=request.args.get('character')
            return redirect(url_for('testBackend', resultado=Character.name(Character.get(idCharacter=character))))
    
    @app.route('/getEpisode', methods=['GET', 'POST'])
    def getEpisode():
        if request.method == 'POST':
            episode=request.args.get('episode')
            return redirect(url_for('testBackend', resultado=Episode.name(Episode.get(idEpisode=episode))))
    
    @app.route('/getLocation', methods=['GET', 'POST'])
    def getLocation():
        if request.method == 'POST':
            location=request.args.get('location')
            return redirect(url_for('testBackend', resultado=Location.name(Location.get(idLocation=location))))


    return app