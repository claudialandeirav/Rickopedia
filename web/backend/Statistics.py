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
    def getGenderCharacterInfo():
        gender_info = {}

        for character in Character.results(Character.getAll()):
            gender = character["gender"]
            if gender in gender_info:
                gender_info[gender] += 1
            else:
                gender_info[gender] = 1

        return gender_info
    
    '''
    Funcion graphicGenderCharacterInfo
    Autora: Claudia Laneira

    Crea el gráfico de los datos de genero de los personajes
    '''
    def graphicGenderCharacterInfo():
        gender_data = Statistics.getGenderCharacterInfo()
        labels = list(gender_data.keys())
        sizes = list(gender_data.values())

        colors = ['#007bff', '#4e73df', '#2e59d9']

        plt.figure(figsize=(5, 5))

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=160, colors=colors)
        plt.setp(ax.texts, size=18)
        ax.axis('equal')
        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        return base64.b64encode(buffer.getvalue()).decode()
