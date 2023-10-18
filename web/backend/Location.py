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