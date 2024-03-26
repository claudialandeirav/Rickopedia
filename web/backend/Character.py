from web.backend.Global import Global
import re

'''
Clase Character
Autora: Claudia Landeira

Información de los personajes
'''
class Character:
    
    '''
    Funcion getAllPaged
    Autora: Claudia Landeira

    Devuelve todos los personajes disponibles y sus datos paginados
    '''
    def getAllPaged(page):
        return Global.data(f"{Global.getUrlCharacter()}?page={page}")

    '''
    Funcion get
    Autora: Claudia Landeira

    Devuelve los datos de un personaje por su id
    '''
    def getById(idCharacter):
        return Global.data(f"{Global.getUrlCharacter()}{idCharacter}")
    
    '''
    Funcion getByList
    Autora: Claudia Landeira

    Devuelve los datos de los personajes por lista de ids
    '''
    def getByList(lista):
        return Global.data(f"{Global.getUrlCharacter()}{lista}")

    '''
    Funcion getAll
    Autora: Claudia Landeira

    Devuelve toda la informacion
    '''
    def getAll():
        return Global.data(Global.getUrlCharacter())

    '''
    Funcion filter
    Autora: Claudia Landeira

    Devuelve toda la información dando la posiiblidad de filtrar por nombre, estatus, especie, tipo o genero
    Todos los parámetros son optativos
    '''
    def filter(name=None, status=None, species=None, type=None, gender=None):        
        param = {}

        if name:
            param["name"] = name
        if status :
            param["status"] = status
        if species:
            param["species"] = species
        if type :
            param["type"] = type
        if gender:
            param["gender"] = gender

        filter = '&'.join(f'{key}={value}' for key, value in param.items())

        if filter:
            url = f'{Global.getUrlCharacter()}?{filter}'

        return Global.data(url)
    
    '''
    Funcion info
    Autora: Claudia Landeira

    Devuelve la información del numero de paginas y de personajes disponibles
    '''
    def info(data):
        info = data['info']
        count = Character.count(info)
        pages = Character.pages(info)
        next = Character.next(info)
        prev = Character.prev(info)
        return {'count': count, 'pages': pages, 'next': next, 'prev': prev}
    
    '''
    Funcion origin
    Autora: Claudia Landeira

    Devuelve la información del planeta origen del personaje
    '''
    def origin(data):
        origin = data['origin']
        name = Character.name(origin)
        url = Character.url(origin)
        id = None
        originId = re.search(r'/(\d+)$', url)
        if (originId):
            id = originId.group(1)
        return {'name': name, 'id': id}
    
    '''
    Funcion location
    Autora: Claudia Landeira

    Devuelve la información de la ultima localizacion conocida del personaje
    '''
    def location(data):
        location = data["location"]
        name = Character.name(location)
        url = Character.url(location)
        id = None
        locationId = re.search(r'/(\d+)$', url)
        if (locationId):
            id = locationId.group(1)
        return {'name': name, 'id': id}
        
    '''
    Funcion results
    Autora: Claudia Landeira

    Devuelve la información completa del personaje
    '''
    def results(data):
        return data['results']
    
    '''
    Funcion count
    Autora: Claudia Landeira

    Devuelve la información del número de personajes
    '''
    def count(data):
        return data['count']
    
    '''
    Funcion pages
    Autora: Claudia Landeira

    Devuelve la información del número de páginas
    '''
    def pages(data):
        return data['pages']
    
    '''
    Funcion next
    Autora: Claudia Landeira

    Devuelve la url de la pagina siguiente
    '''
    def next(data):
        return data['next']
    
    '''
    Funcion prev
    Autora: Claudia Landeira
    
    Devuelve la url de la pagina anterior
    '''
    def prev(data):
        return data['prev']
    
    '''
    Funcion id
    Autora: Claudia Landeira

    Devuelve el id del personaje    
    '''
    def id(data):
        return data['id']
    
    '''
    Funcion name
    Autora: Claudia Landeira

    Devuelve el nombre del personaje
    '''
    def name(data):
        return data['name']
    
    '''
    Funcion url
    Autora: Claudia Landeira

    Devuelve la url del personaje
    '''
    def url(data):
        return data['url']
    
    '''
    Funcion status
    Autora: Claudia Landeira

    Devuelve el estado del personaje
    '''
    def status(data):
        return data['status']
    
    '''
    Funcion species
    Autora: Claudia Landeira

    Devuelve la especie del personaje
    '''
    def species(data):
        return data['species']
    
    '''
    Funcion type
    Autora: Claudia Landeira

    Devuelve el tipo del personaje
    '''
    def type(data):
        return data['type']
    
    '''
    Funcion gender
    Autora: Claudia Landeira

    Devuelve el genero del personaje
    '''
    def gender(data):
        return data['gender']
    
    '''
    Funcion image
    Autora: Claudia Landeira

    Devuelve la imagen del personaje
    '''    
    def image(data):
        return data['image']
    
    '''
    Funcion episode
    Autora: Claudia Landeira

    Devuelve el listado de los episodios en los que aparece el personaje
    '''
    def episode(data):
        urls = data['episode']
        episodeIds = []
        for i in urls:
            episodeId = re.search(r'/(\d+)$', i).group(1)
            episodeIds.append(episodeId)
        return list(map(int, episodeIds))
    