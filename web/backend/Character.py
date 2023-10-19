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
    def get_all(self):
        return Global.data(Global.getUrlCharacter())
    
    '''
    Function get
    Author: Claudia Landeira

    It has the responsability of get a character by id
    '''
    def get(self, idCharacter):
        return Global.data(f"{Global.getUrlCharacter()}{idCharacter}")
    
    '''
    Function filter
    Author: Claudia Landeira

    It has the responsability of get the information filtering by name, status, species, type or gender
    '''
    def filter(self, name=None, status=None, species=None, type=None, gender=None):        
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
    def info(self, data):
        info = data['info']
        count = Character.count(info)
        pages = Character.pages(info)

        return [count, pages]
    
    '''
    Function origin
    Author: Claudia Landeira

    It has the responsability of get origin param of info param on json data
    '''
    def origin(self, data):
        origin = data['origin']
        name = Character.name(origin)
        url = Character.url(origin)

        return [name, url]
    
    '''
    Function location
    Author: Claudia Landeira

    It has the responsability of get location param of info param on json data
    '''
    def location(self, data):
        location = data['location']
        name = Character.name(location)
        url = Character.url(location)

        return [name, url]
        
    '''
    Function results
    Author: Claudia Landeira

    It has the responsability of get results param of info param on json data
    '''
    def results(self, data):
        return data['results']
    
    '''
    Function count
    Author: Claudia Landeira

    It has the responsability of get count param of info param on json data
    '''
    def count(self, data):
        return data['count']
    
    '''
    Function pages
    Author: Claudia Landeira

    It has the responsability of get pages param of info param on json data
    '''
    def pages(self, data):
        return data['pages']
    
    '''
    Function id
    Author: Claudia Landeira

    It has the responsability of get id param of info param on json data
    '''
    def id(self, data):
        return data['id']
    
    '''
    Function name
    Author: Claudia Landeira

    It has the responsability of get name param of info param on json data
    '''
    def name(self, data):
        return data['name']
    
    '''
    Function url
    Author: Claudia Landeira

    It has the responsability of get url param of info param on json data
    '''
    def url(self, data):
        return data['url']
    
    '''
    Function status
    Author: Claudia Landeira

    It has the responsability of get status param of info param on json data
    '''
    def status(self, data):
        return data['status']
    
    '''
    Function species
    Author: Claudia Landeira

    It has the responsability of get species param of info param on json data
    '''
    def species(self, data):
        return data['species']
    
    '''
    Function type
    Author: Claudia Landeira

    It has the responsability of get type param of info param on json data
    '''
    def type(self, data):
        return data['type']
    
    '''
    Function gender
    Author: Claudia Landeira

    It has the responsability of get gender param of info param on json data
    '''
    def gender(self, data):
        return data['gender']
    
    '''
    Function image
    Author: Claudia Landeira

    It has the responsability of get image param of info param on json data
    '''    
    def image(self, data):
        return data['image']
    
    '''
    Function episode
    Author: Claudia Landeira

    It has the responsability of get episode param of info param on json data
    '''
    def episode(self, data):
        return data['episode']
    