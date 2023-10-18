from web.backend.Global import Global

class Episode:

    def get_all(self):
        return Global.data(Global.getUrlEpisode())
    
    def get(self, idEpisode):
        return Global.data(f'{Global.getUrlEpisode()}{idEpisode}')
    
    def filter(self, name=None, air_date=None, episode=None):
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
    
    def info(self, data):
        info = data['info']
        count = Episode.count(info)
        pages = Episode.pages(info)
        
        return [count, pages]
    
    def count(self, data):
        return data['count']
    
    def pages(self, data):
        return data['pages']
    
    def results(self, data):
        return data['results']
    
    def id(self, data):
        return data['id']
    
    def name(self, data):
        return data['name']
    
    def air_date(self, data):
        return data['air_date']
    
    def episode(self, data):
        return data['episode']
    
    def characters(self, data):
        return data['characters']