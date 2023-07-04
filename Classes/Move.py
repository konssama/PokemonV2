from Api.RequestMove import requestMove
from Classes.Type import Type

class Move:
    def __init__(self, move: str):
        self.name = move.title()
        self.response = requestMove(move)

        self.type = Type(self.response['type']['name'])
        self.accuracy = self.response['accuracy']
        self.damageClass = self.response['damage_class']['name']
        self.power = self.response['power']
        self.pp = self.response['pp']
        self.priority = self.response['priority'] #0 normally, 1 for attacks like Quick Attack

        #effects

    def __str__(self) -> str:
        st = ""
        st += "Name: " + self.name + "\n"
        st += "Type: " + self.type + "\n"
        st += "Accuracy: " + self.accuracy + "\n"
        st += "Damage Class: " + self.damageClass + "\n"
        st += "Power: " + self.power + "\n"
        st += "PP: " + self.pp + "\n"
        st += "Priority: " + self.priority + "\n"

        st += "------------------------------------------------------------"
        
        return st