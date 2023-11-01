from web.backend.Global import Global

'''
Class Character
Author: Claudia Landeira

It has the responsability of get the information about the character
'''
class Character:

    '''
    Function get_all
    Author: Claudia Landeira

    It has the responsability of get all character of Rick and Morty
    '''
    def get_all():
        return Global.data(Global.getUrlCharacter())
    
    '''
    Function get
    Author: Claudia Landeira

    It has the responsability of get a character by id
    '''
    def get(idCharacter):
        return Global.data(f"{Global.getUrlCharacter()}{idCharacter}")
    
    '''
    Function filter
    Author: Claudia Landeira

    It has the responsability of get the information filtering by name, status, species, type or gender
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
    Function info
    Author: Claudia Landeira

    It has the responsability of get info param on json data
    '''
    def info(data):
        info = data['info']
        count = Character.count(info)
        pages = Character.pages(info)

        return [count, pages]
    
    '''
    Function origin
    Author: Claudia Landeira

    It has the responsability of get origin param of info param on json data
    '''
    def origin(data):
        origin = data['origin']
        name = Character.name(origin)
        url = Character.url(origin)

        return [name, url]
    
    '''
    Function location
    Author: Claudia Landeira

    It has the responsability of get location param of info param on json data
    '''
    def location(data):
        location = data['location']
        name = Character.name(location)
        url = Character.url(location)

        return [name, url]
        
    '''
    Function results
    Author: Claudia Landeira

    It has the responsability of get results param of info param on json data
    '''
    def results(data):
        return data['results']
    
    '''
    Function count
    Author: Claudia Landeira

    It has the responsability of get count param of info param on json data
    '''
    def count(data):
        return data['count']
    
    '''
    Function pages
    Author: Claudia Landeira

    It has the responsability of get pages param of info param on json data
    '''
    def pages(data):
        return data['pages']
    
    '''
    Function id
    Author: Claudia Landeira

    It has the responsability of get id param of info param on json data
    '''
    def id(data):
        return data['id']
    
    '''
    Function name
    Author: Claudia Landeira

    It has the responsability of get name param of info param on json data
    '''
    def name(data):
        return data['name']
    
    '''
    Function url
    Author: Claudia Landeira

    It has the responsability of get url param of info param on json data
    '''
    def url(data):
        return data['url']
    
    '''
    Function status
    Author: Claudia Landeira

    It has the responsability of get status param of info param on json data
    '''
    def status(data):
        return data['status']
    
    '''
    Function species
    Author: Claudia Landeira

    It has the responsability of get species param of info param on json data
    '''
    def species(data):
        return data['species']
    
    '''
    Function type
    Author: Claudia Landeira

    It has the responsability of get type param of info param on json data
    '''
    def type(data):
        return data['type']
    
    '''
    Function gender
    Author: Claudia Landeira

    It has the responsability of get gender param of info param on json data
    '''
    def gender(data):
        return data['gender']
    
    '''
    Function image
    Author: Claudia Landeira

    It has the responsability of get image param of info param on json data
    '''    
    def image(data):
        return data['image']
    
    '''
    Function episode
    Author: Claudia Landeira

    It has the responsability of get episode param of info param on json data
    '''
    def episode(data):
        return data['episode']
    