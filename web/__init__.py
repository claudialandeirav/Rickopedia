from flask import Flask, render_template, request

from web.backend.Character import Character
from web.backend.Episode import Episode
from web.backend.Location import Location
from web.backend.Statistics import Statistics
from web.backend.Global import Global

def start_app():
    app = Flask(__name__, static_folder='static')
    app.secret_key='estoesunaclavesupersecreta'

    episodesSummary = Episode.getEpisodesSummary();

    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')

    # ---------------------------------- MODULO PERSONAJES
    @app.route('/characters', methods=['GET', 'POST'])
    def characters():
        if request.method == 'POST':
            filter = request.form

            characters = {}
            if (filter != {}):
                allInfo, url = Character.filter(filter)
                if ('error' not in allInfo):
                    characters = Character.getAllNotPagedBydata(allInfo, url)

            return render_template('characters.html', characters=characters, page=0)

        else:
            page = request.args.get('page', default=1, type=int)
            characters = Character.results(Character.getAllPaged(Global.getUrlCharacter(),page))

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
        numCharacters = Character.count(Character.info(Character.getAll()))

        return render_template('character.html', id=int(id), name=name, status=status, species=species, type=type, gender=gender,
                                origin=origin, location=location, image=image, episodes=episodes, numCharacters=numCharacters)
    
    # ---------------------------------- MODULO EPISODIOS
    @app.route('/episodes', methods=['GET'])
    def episodes():
        seasons = Episode.getEpisodes()
        return render_template('episodes.html', seasons=seasons)
    
    @app.route('/episode/<id>', methods=['GET'])
    def episode(id):
        episode = Episode.getById(id)
        name = Episode.name(episode)
        air_date = Episode.air_date(episode)
        episode_code = Episode.episode(episode)        
        characters = Character.getByList(Episode.character(episode))
        summary = Episode.getSummary(episodesSummary, id)
        seasons = Episode.getEpisodes()
        numEpisodes = Episode.count(Episode.info(Episode.getAll()))

        return render_template('episode.html', id=int(id), name=name, air_date=air_date, episode_code=episode_code, characters=characters, summary=summary, seasons=seasons, numEpisodes=numEpisodes)

    # ---------------------------------- MODULO LOCALIZACIONES
    @app.route('/locations', methods=['GET'])
    def locations():
        page = request.args.get('page', default=1, type=int)
        locations = Location.results(Location.getAllPaged(page))

        return render_template('locations.html', locations=locations, page=page)
    
    @app.route('/location/<id>', methods=['GET'])
    def location(id):
        location = Location.getById(id)
        name = Location.name(location)
        type = Location.type(location)
        dimension = Location.dimension(location)
        residents = Character.getByList(Location.residents(location))
        numLocations = Location.count(Location.info(Location.getAll()))

        return render_template('location.html', id=int(id), name=name, type=type, dimension=dimension, residents=residents, numLocations=numLocations)

    # ---------------------------------- MODULO STATISTICS
    @app.route('/statistics', methods=['GET'])
    def statistics():
        numEpisodes = Statistics.getNumEpisodes()
        numLocations = Statistics.getNumLocations()
        numCharacters = Statistics.getNumCharacters()

        allCharacters = Character.getAllNotPaged()
        allLocations = Location.getAllNotPaged()
        
        genderCharacterInfo = Statistics.createCircularGraphic(Statistics.getGenderCharacterInfo(allCharacters))
        statusCharacterInfo = Statistics.createCircularGraphic(Statistics.getStatusCharacterInfo(allCharacters))
        
        genderNumInfo = Statistics.getNumGenderInfo(allCharacters)
        statusNumInfo = Statistics.getNumStatusInfo(allCharacters)
        speciesNumInfo = Statistics.getNumSpecieInfo(allCharacters)

        typeNumInfo = Statistics.getNumTypeInfo(allLocations)
        dimensionNumInfo = Statistics.getNumDimensionsInfo(allLocations)
        
        episodesPerSeasonNumInfo = Statistics.getEpisodesPerSeasonInfo()

        return render_template('statistics.html', 
                               numEpisodes = int(numEpisodes), numLocations = int(numLocations), numCharacters = int(numCharacters),
                               genderCharacterInfo = genderCharacterInfo, genderNumInfo = genderNumInfo,
                               statusCharacterInfo = statusCharacterInfo, statusNumInfo = statusNumInfo,
                               speciesNumInfo = speciesNumInfo, typeNumInfo = typeNumInfo, dimensionNumInfo = dimensionNumInfo,
                               episodesPerSeasonNumInfo = episodesPerSeasonNumInfo)
    
    # ---------------------------------- MODULO ABOUT
    @app.route('/about', methods=['GET'])
    def about():
        return render_template('about.html')
    
    return app