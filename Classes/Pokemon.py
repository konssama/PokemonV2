from Classes.Type import Type
from Classes.Move import Move
from Api.RequestPokemon import requestPokemon


class Pokemon:
    def __init__(self, name: str):
        self.name = name.title()
        self.response = requestPokemon(name)

        # images
        self.imageFront = self.response["sprites"]["versions"]["generation-v"][
            "black-white"
        ]["front_default"]
        self.imageBack = self.response["sprites"]["versions"]["generation-v"][
            "black-white"
        ]["back_default"]

        # types
        self.types = []
        for i in self.response["types"]:
            self.types.append(Type(i["type"]["name"]))

        # stats
        self.stats = []  # hp, attack, defense, sp.attack, sp.defense, speed
        for i in self.response["stats"]:
            self.stats.append(i["base_stat"])

        # moves
        self.moves = []

    def __str__(self) -> str:
        st = ""
        st += "Name:" + self.name + "\n"
        st += "Types: "
        for i in self.types:
            st += str(i) + "\n"
        st += "Stats: " + "\n"
        for i in self.stats:
            st += str(i) + ","
        st += "\n"
        st += "Moves: " + "\n"
        for i in self.moves:
            st += str(i) + ","
        st += "\n"

        st += "------------------------------------------------------------"

        return st
