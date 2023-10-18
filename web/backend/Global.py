from flask import Flask, jsonify
import requests

class Global:

    def getUrlCharacter():
        return 'https://rickandmortyapi.com/api/character/'
    
    def getUrlLocation():
        return 'https://rickandmortyapi.com/api/location/'
    
    def getUrlEpisode():
        return 'https://rickandmortyapi.com/api/episode/'
    

    def data(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

        return data