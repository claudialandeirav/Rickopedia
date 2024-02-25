from flask import Flask, jsonify
import requests

'''
Clase Global
Autora: Claudia Landeira

Información que afecta a todas las demás clases
'''
class Global:

    '''
    Funcion getUrlCharacter
    Autora: Claudia Landeira

    Devuelve la url de los personajes
    '''
    def getUrlCharacter():
        return 'https://rickandmortyapi.com/api/character/'
    
    '''
    Funcion getUrlLocation
    Autora: Claudia Landeira

    Devuelve la url de los localizaciones
    '''
    def getUrlLocation():
        return 'https://rickandmortyapi.com/api/location/'
    
    '''
    Funcion getUrlEpisode
    Autora: Claudia Landeira

    Devuelve la url de los episodios
    '''
    def getUrlEpisode():
        return 'https://rickandmortyapi.com/api/episode/'
    
    '''
    Funcion data
    Autora: Claudia Landeira

    Hace la request a la url y devuelve los datos en formato json
    '''
    def data(url):
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

        return data