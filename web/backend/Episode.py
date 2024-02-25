from web.backend.Global import Global

'''
Clase Episode
Autora: Claudia Landeira

Informacion de los episodios
'''
class Episode:

    '''
    Funcion get_all
    Autora: Claudia Landeira

    Devuelve todos los episodios disponibles y sus datos
    '''
    def get_all():
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
    def filter(name=None, air_date=None, episode=None):
        param = {}

        if name:
            param['name'] = name
        if air_date:
            param['air_date'] = air_date
        if episode:
            param['episode'] = episode

        filter = '&'.join(f'{key}={value}' for key, value in param.items())

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
    Funcion characters
    Autora: Claudia Landeira

    Devuelve el listado de personajes que aparecen en el episodio
    '''
    def characters(data):
        return data['characters']
    
    '''
    Funcion getEpisodes
    Autora: Claudia Landeira

    Devuelve un listado de los episodios y sus datos separados por temporadas
    '''
    def getEpisodes(episodes):
        seasons = {}
        for episode in episodes:
            season_num = episode['episode'][:3]
            if season_num not in seasons:
                seasons[season_num] = []
            seasons[season_num].append(episode)
        return seasons