from web.backend.Global import Global

class Location:
    
    def get_all(self):
        return Global.data(Global.getUrlLocation())
    
    def get(self, idLocation):
        return Global.data(f'{Global.getUrlLocation()}{idLocation}')
    
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
    

    def info(self, data):
        info = data['info']
        count = Location.count(info)
        pages = Location.pages(info)
        
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
    
    def type(self, data):
        return data['type']
    
    def dimension(self, data):
        return data['dimension']
    
    def residents(self, data):
        return data['residents']