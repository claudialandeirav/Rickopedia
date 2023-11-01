from web.backend.Global import Global

'''
Class Episode
Author: Claudia Landeira

It has the responsability of get the information about the episode
'''
class Episode:

    '''
    Function get_all
    Author: Claudia Landeira

    It has the responsability of get all character of Rick and Morty
    '''
    def get_all():
        return Global.data(Global.getUrlEpisode())
    
    '''
    Function get
    Author: Claudia Landeira

    It has the responsability of get a character by id
    '''
    def get(idEpisode):
        return Global.data(f'{Global.getUrlEpisode()}{idEpisode}')
    
    '''
    Function filter
    Author: Claudia Landeira

    It has the responsability of get the information filtering by name, status, species, type or gender
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
    Function info
    Author: Claudia Landeira

    It has the responsability of get info param on json data
    '''
    def info(data):
        info = data['info']
        count = Episode.count(info)
        pages = Episode.pages(info)
        
        return [count, pages]
    
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
    Function results
    Author: Claudia Landeira

    It has the responsability of get results param of info param on json data
    '''
    def results(data):
        return data['results']
    
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
    Function air_date
    Author: Claudia Landeira

    It has the responsability of get air date param of info param on json data
    '''
    def air_date(data):
        return data['air_date']
    
    '''
    Function episode
    Author: Claudia Landeira

    It has the responsability of get episode param of info param on json data
    '''
    def episode(data):
        return data['episode']
    
    '''
    Function characters
    Author: Claudia Landeira

    It has the responsability of get characters param of info param on json data
    '''
    def characters(data):
        return data['characters']