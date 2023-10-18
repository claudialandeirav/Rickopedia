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
