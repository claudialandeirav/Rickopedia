from web.backend.Global import Global

class Character:

    def get_all(self):
        return Global.data(Global.getUrlCharacter())
    
    def get(self, idCharacter):
        return Global.data(f"{Global.getUrlCharacter()}{idCharacter}")
    
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
    
    def info(self, data):
        info = data['info']
        count = Character.count(info)
        pages = Character.pages(info)

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
    
    def status(self, data):
        return data['status']
    
    def species(self, data):
        return data['species']
    
    def type(self, data):
        return data['type']
    
    def gender(self, data):
        return data['gender']
    
    def origin(self, data):
        origin = data['origin']
        name = Character.nameOrigin(origin)
        url = Character.urlOrigin(origin)

        return [name, url]
    
    def nameOrigin(self, data):
        return data['name']
    
    def urlOrigin(self, data):
        return data['url']
    
    def location(self, data):
        location = data['location']
        name = Character.nameLocation(location)
        url = Character.urlLocation(location)

        return [name, url]
    
    def nameLocation(self, data):
        return data['name']
    
    def urlLocation(self, data):
        return data['url']
    
    def image(self, data):
        return data['image']
    
    def episode(self, data):
        return data['episode']
    