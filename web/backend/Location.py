from web.backend.Global import Global

'''
Class Location
Author: Claudia Landeira

It has the responsability of get the information about the location
'''
class Location:
    
    '''
    Function get_all
    Author: Claudia Landeira

    It has the responsability of get all character of Rick and Morty
    '''
    def get_all(self):
        return Global.data(Global.getUrlLocation())
    
    '''
    Function get
    Author: Claudia Landeira

    It has the responsability of get a character by id
    '''
    def get(self, idLocation):
        return Global.data(f'{Global.getUrlLocation()}{idLocation}')
    
    '''
    Function filter
    Author: Claudia Landeira

    It has the responsability of get the information filtering by name, status, species, type or gender
    '''
    def filter(self, name=None, type=None):
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
    Function info
    Author: Claudia Landeira

    It has the responsability of get info param on json data
    '''
    def info(self, data):
        info = data['info']
        count = Location.count(info)
        pages = Location.pages(info)
        
        return [count, pages]
    
    '''
    Function count
    Author: Claudia Landeira

    It has the responsability of get count param of info param on json data
    '''
    def count(self, data):
        return data['count']
    
    '''
    Function id
    Author: Claudia Landeira

    It has the responsability of get id param on json data
    '''
    def id(self, data):
        return data['pages']
    
    '''
    Function results
    Author: Claudia Landeira

    It has the responsability of get results param of info param on json data
    '''
    def results(self, data):
        return data['results']
    
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
    Function type
    Author: Claudia Landeira

    It has the responsability of get type param of info param on json data
    '''
    def type(self, data):
        return data['type']
    
    '''
    Function dimension
    Author: Claudia Landeira

    It has the responsability of get dimension param of info param on json data
    '''
    def dimension(self, data):
        return data['dimension']
    
    '''
    Function residents
    Author: Claudia Landeira

    It has the responsability of get residents param of info param on json data
    '''
    def residents(self, data):
        return data['residents']