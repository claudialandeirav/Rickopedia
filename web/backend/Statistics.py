from web.backend.Global import Global
from web.backend.Character import Character
from web.backend.Location import Location
from web.backend.Episode import Episode

import matplotlib.pyplot as plt
from io import BytesIO
import base64

'''
Clase Statistics
Autora: Claudia Landeira

Información estadística de los datos obtenidos de la API
'''
class Statistics:
    

    '''
    Funcion getNumEpisodes
    Autora: Claudia Landeira

    Devuelve los datos de un personaje por su id
    '''
    def getNumEpisodes():
        return Episode.count(Episode.info(Episode.getAll()));
    
    '''
    Funcion getNumCharacters
    Autora: Claudia Landeira

    Devuelve los datos de un personaje por su id
    '''
    def getNumCharacters():
        return Character.count(Character.info(Character.getAll()))
    
    '''
    Funcion getNumLocations
    Autora: Claudia Landeira

    Devuelve los datos de un personaje por su id
    '''
    def getNumLocations():
        return Location.count(Location.info(Location.getAll()))
    
    '''
    Funcion getGenderCharacterInfo
    Autora: Claudia Landeira

    Devuelve al frecuencia de genero de los personajes
    '''
    def getGenderCharacterInfo(allCharacters):
        gender_info = {}

        for character in allCharacters:
            gender = character["gender"]
            if gender in gender_info:
                gender_info[gender] += 1
            else:
                gender_info[gender] = 1

        return gender_info
    
    def getNumGenderInfo(allCharacters):
        gender_info = Statistics.getGenderCharacterInfo(allCharacters)
        return gender_info

    '''
    Funcion getStatusCharacterInfo()
    Autora: Claudia Landeira

    Devuelve la frecuencia de estatus de los personajes
    '''
    def getStatusCharacterInfo(allCharacters):
        status_info = {}

        for character in allCharacters:
            status = character["status"]
            if status in status_info:
                status_info[status] += 1
            else:
                status_info[status] = 1

        return status_info

    def getNumStatusInfo(allCharacters):
        gender_info = Statistics.getStatusCharacterInfo(allCharacters)
        return gender_info
    
    '''
    Funcion getSpeciesCharacterInfo()
    Autora: Claudia Landeira

    Devuelve la frecuencia de especies de los personajes
    '''
    def getSpeciesCharacterInfo(allCharacters):
        species_info = {}

        for character in allCharacters:
            specie = character['species']
            if specie in species_info:
                species_info[specie] += 1
            else:
                species_info[specie] = 1

        return species_info

    def getNumSpecieInfo(allCharacters):
        specie_info = Statistics.getSpeciesCharacterInfo(allCharacters)
        return specie_info
    
    
    '''
    Funcion getTypesLocationsInfo()
    Autora: Claudia Landeira

    Devuelve la frecuencia de tipos de localizaciones
    '''
    def getTypesLocationsInfo(allLocations):
        type_info = {}

        for location in allLocations:
            type = location['type']
            if type in type_info:
                type_info[type] += 1
            else:
                type_info[type] = 1

        return type_info
    
    def getNumTypeInfo(allLocations):
        type_info = Statistics.getTypesLocationsInfo(allLocations)
        return type_info
    

    '''
    Funcion getTypesLocationsInfo()
    Autora: Claudia Landeira

    Devuelve la frecuencia de tipos de localizaciones
    '''
    def getDimensionsLocationsInfo(allLocations):
        dimension_info = {}

        for location in allLocations:
            dimension = location['dimension']
            if dimension in dimension_info:
                dimension_info[dimension] += 1
            else:
                dimension_info[dimension] = 1

        return dimension_info
    
    def getNumDimensionsInfo(allLocations):
        dimension_info = Statistics.getDimensionsLocationsInfo(allLocations)
        return dimension_info
    

    def getEpisodesPerSeasonInfo():
        episodesPerSeason = Episode.getEpisodes()
        season_info = {}

        for season, episodes in episodesPerSeason.items():
            season_info[season] = len(episodes)

        return season_info

    '''
    Funcion createCircularGraphic
    Autora: Claudia Laneira

    Crea el gráfico circular con los datos introducidos por parámetros
    '''
    def createCircularGraphic(data):
        colors = ['#ADD8E6', '#4682B4', '#1E90FF', '#008B8B', '#5F9EA0', '#4B0082', '#6A5ACD', '#4169E1', '#000080', '#87CEEB']

        labels = list(data.keys())
        sizes = list(data.values())

        plt.figure(figsize=(5, 5))

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=160, colors=colors)
        plt.setp(ax.texts, size=18)
        ax.axis('equal')
        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        return base64.b64encode(buffer.getvalue()).decode()
