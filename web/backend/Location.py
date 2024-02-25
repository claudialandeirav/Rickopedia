from web.backend.Global import Global

'''
Clase Location
Autora: Claudia Landeira

Informacion de las localizaciones
'''
class Location:
    
    '''
    Funcion get_all
    Autora: Claudia Landeira

    Devuelve toda la informacion de las localizaciones disponibles
    '''
    def get_all():
        return Global.data(Global.getUrlLocation())
    
    '''
    Funcion get
    Autora: Claudia Landeira

    Devuelve toda la información por id
    '''
    def getById(idLocation):
        return Global.data(f'{Global.getUrlLocation()}{idLocation}')
    
    '''
    Funcion filter
    Autora: Claudia Landeira

    Devuelve toda la información dando la posiiblidad de filtrar por nombre y/o tipo
    Todos los parametros son optativos
    '''
    def filter(name=None, type=None):
        param = {}

        if name:
            param['name'] = name
        if type:
            param['type'] = type

        filter = '&'.join(f'{key}={value}' for key, value in param.items())

        if filter:
            url = f'{Global.getUrlLocation()}?{filter}'

        return Global.data(url)
    
    '''
    Funcion info
    Autora: Claudia Landeira

    Devuelve la información referente al numero de localizaciones y su paginacion
    '''
    def info(data):
        info = data['info']
        count = Location.count(info)
        pages = Location.pages(info)
        
        return [count, pages]
    
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
        return data['residents']