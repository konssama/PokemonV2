from Api.RequestPokemon import requestPokemon
from Classes.Type import Type

class Pokemon:
    def __init__(self, name):
        self.name = name.title()
        self.response = requestPokemon(name)
        
        #images
        self.imageFront = self.response['sprites']['versions']['generation-v']['black-white']['front_default']
        self.imageBack = self.response['sprites']['versions']['generation-v']['black-white']['back_default']

        #types
        self.types = []
        for i in self.response['types']:
            self.types.append(Type(i['type']['name']))

        #stats
        self.stats = [] #hp, attack, defense, sp.attack, sp.defense, speed
        for i in self.response['stats']:
            self.stats.append(i['base_stat'])

        #moves
        self.moves = "move"