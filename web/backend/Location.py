from web.backend.Global import Global
import re
import requests


'''
Clase Location
Autora: Claudia Landeira

Informacion de las localizaciones
'''
class Location:
    
    '''
    Funcion getAllPaged
    Autora: Claudia Landeira

    Devuelve todos las localizacinos disponibles y sus datos paginados
    '''
    def getAllPaged(page):
        return Global.data(f"{Global.getUrlLocation()}?page={page}")
    
    '''
    Funcion getAllNotPaged
    Autora: Claudia Landeira

    Obtener todos las localizaciones no paginados
    '''
    def getAllNotPaged():
        url = Global.getUrlLocation()
        locations = []
        
        while url:
            data = requests.get(url).json()
            locations.extend(data['results'])
            url = data['info']['next']

        return locations

    def getAllNotPagedBydata(data, filters):
        url = f'{Global.getUrlLocation()}?page=1&{filters}'
        locations = []
        
        while url:
            data = requests.get(url).json()
            locations.extend(data['results'])
            url = data['info']['next']

        return locations
    '''
    Funcion get
    Autora: Claudia Landeira

    Devuelve toda la información por id
    '''
    def getById(idLocation):
        return Global.data(f'{Global.getUrlLocation()}{idLocation}')
    
    '''
    Funcion getByList
    Autora: Claudia Landeira

    Devuelve toda la informacion por lista
    '''
    def getByList(lista):
        return Global.data(f'{Global.getUrlLocation()}{lista}')

    '''
    Funcion getAll
    Autora: Claudia Landeira

    Devuelve toda la informacion
    '''
    def getAll():
        return Global.data(Global.getUrlLocation())

    '''
    Funcion filter
    Autora: Claudia Landeira

    Devuelve toda la información dando la posiiblidad de filtrar por nombre y/o tipo
    Todos los parametros son optativos
    '''
    def filter (filters=None):
        filter = '&'.join(f'{key}={value}' for key, value in filters.items())
        if filter:
            url = f'{Global.getUrlLocation()}?{filter}'

        return Global.data(url), filter
    
    '''
    Funcion info
    Autora: Claudia Landeira

    Devuelve la información referente al numero de localizaciones y su paginacion
    '''
    def info(data):
        info = data['info']
        count = Location.count(info)
        pages = Location.pages(info)
        
        return {'count': count, 'pages': pages}
    
    '''
    Funcion count
    Autora: Claudia Landeira

    Devuelve el numero de localizaciones
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

    Devuelve el valor de los resultados de la localizacion
    '''
    def results(data):
        return data['results']
    
    '''
    Funcion id
    Autora: Claudia Landeira

    Devuelve el id de la localizacion
    '''
    def id(data):
        return data['id']
    
    '''
    Funcion name
    Autora: Claudia Landeira

    Devuelve el nombre de la localizacion
    '''
    def name(data):
        return data['name']
    
    '''
    Funcion type
    Autora: Claudia Landeira

    Devuelve el tipo de localizacion
    '''
    def type(data):
        return data['type']
    
    '''
    Funcion dimension
    Autora: Claudia Landeira

    Devuelve la dimension de la localizacion
    '''
    def dimension(data):
        return data['dimension']
    
    '''
    Funcion residents
    Autora: Claudia Landeira

    Devuelve el listado de personajes de esa localizacion
    '''
    def residents(data):
        urls = data['residents']
        residentIds = []
        for i in urls:
            residentId = re.search(r'/(\d+)$', i).group(1)
            residentIds.append(residentId)
        return list(map(int, residentIds))
    