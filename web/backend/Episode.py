from web.backend.Global import Global
import json
import re

'''
Clase Episode
Autora: Claudia Landeira

Informacion de los episodios
'''
class Episode:

    '''
    Funcion getAll
    Autora: Claudia Landeira

    Devuelve todos los episodios disponibles y sus datos
    '''
    def getAll():
        return Global.data(Global.getUrlEpisode())
    
    '''
    Funcion get
    Autora: Claudia Landeira

    Devuelve los datos de un episodio por su id
    '''
    def getById(idEpisode):
        return Global.data(f'{Global.getUrlEpisode()}{idEpisode}')
    
    '''
    Funcion getByList
    Autora: Claudia Landeira

    Devuelve los datos de los episodios por lista de ids
    '''
    def getByList(lista):
        return Global.data(f"{Global.getUrlEpisode()}{lista}")
    
    '''
    Funcion filter
    Autora: Claudia Landeira

    Devuelve toda la información dando la posiiblidad de filtrar por nombre, fecha de salida del episodio o codigo del episodio
    Todos los parametros son optativos
    '''
    def filter (filters=None):
        filter = '&'.join(f'{key}={value}' for key, value in filters.items())
        if filter:
            url = f'{Global.getUrlEpisode()}?{filter}'

        return Global.data(url)
    
    '''
    Funcion info
    Autora: Claudia Landeira

    Devuelve la información referente al número de episodios y su paginacion
    '''
    def info(data):
        info = data['info']
        count = Episode.count(info)
        pages = Episode.pages(info)
        
        return {'count': count, 'pages': pages}
    
    '''
    Funcion count
    Autora: Claudia Landeira

    Devuelve el numero de episodios
    '''
    def count(data):
        return data['count']
    
    '''
    Funcion pages
    Autora: Claudia Landeira

    Devuelve el numero de paginas
    '''
    def pages(data):
        return data['pages']
    
    '''
    Funcion results
    Autora: Claudia Landeira

    Devuelve el valor de los resultados del episodio
    '''
    def results(data):
        return data['results']
    
    '''
    Funcion id
    Autora: Claudia Landeira

    Devuelve el id del episodio
    '''
    def id(data):
        return data['id']
    
    '''
    Funcion name
    Autora: Claudia Landeira

    Devuelve el nombre del episodio
    '''
    def name(data):
        return data['name']
    
    '''
    Funcion air_date
    Autora: Claudia Landeira

    Devuelve la fecha de salida del episodio
    '''
    def air_date(data):
        return data['air_date']
    
    '''
    Funcion episode
    Autora: Claudia Landeira

    Devuelve el codigo del episodio
    '''
    def episode(data):
        return data['episode']
    
    '''
    Funcion getEpisodes
    Autora: Claudia Landeira

    Devuelve un listado de los episodios y sus datos separados por temporadas
    '''
    def getEpisodes():
        numEpisodes = Episode.count(Episode.info(Episode.getAll()))
        listIdEpisodes = [i for i in range(1, numEpisodes + 1)]
        episodes = Episode.getByList(listIdEpisodes)
        seasons = {}
        for episode in episodes:
            season_num = episode['episode'][:3]
            if season_num not in seasons:
                seasons[season_num] = []
            seasons[season_num].append(episode)
        return seasons
    
    '''
    Funcion getEpisode
    Autora: Claudia Landeira

    Devuelve el episodio y con su temporada
    '''
    def getEpisode(episode):
        code = {}
        season_num = episode['episode'][:3]
        episode_num = episode['episode'][-3:]
        code[season_num] = episode_num
        return code
    

    def getEpisodesFilter(data):
        listIdEpisodes = []
        for i in Episode.results(data):
            listIdEpisodes.append(int(i['id']))

        episodes = Episode.getByList(listIdEpisodes)
        seasons = {}
        for episode in episodes:
            season_num = episode['episode'][:3]
            if season_num not in seasons:
                seasons[season_num] = []
            seasons[season_num].append(episode)
        return seasons

    '''
    Funcion getEpisodeDescriptions
    Autora: Claudia Landeira

    Devuelve los datos del archivo /data/episodes.json
    '''
    def getEpisodesSummary():
        with open('./web/data/episodes.json', 'r') as summarys:
            summary = summarys.read()
            datos = json.loads(summary)
        
        return datos
    
    '''
    Funcion getDescription
    Autora: Claudia Landeira

    Devuelve la descripcion del capitulo por su id
    '''
    def getSummary(data, id):
        for d in data:
            if (d["id"] == int(id)):
                return d["summary"]
        
    '''
    Funcion character
    Autora: Claudia Landeira

    Devuelve el listado de los personajes en los que aparece en un episodio
    '''
    def character(data):
        urls = data['characters']
        characterIds = []
        for i in urls:
            characterId = re.search(r'/(\d+)$', i).group(1)
            characterIds.append(characterId)
        return list(map(int, characterIds))