from flask import Flask, jsonify
import requests

'''
Class Global
Author: Claudia Landeira

It has the responsability of process common operations
'''
class Global:

    '''
    Function get_all
    Author: Claudia Landeira

    It has the responsability of get the url of character request
    '''
    def getUrlCharacter():
        return 'https://rickandmortyapi.com/api/character/'
    
    '''
    Function get_all
    Author: Claudia Landeira

    It has the responsability of get the url of location request
    '''
    def getUrlLocation():
        return 'https://rickandmortyapi.com/api/location/'
    
    '''
    Function get_all
    Author: Claudia Landeira

    It has the responsability of get the url of episode request
    '''
    def getUrlEpisode():
        return 'https://rickandmortyapi.com/api/episode/'
    
    '''
    Function get_all
    Author: Claudia Landeira

    It has the responsability of do the request by url and return the data on json format
    '''
    def data(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

        return data