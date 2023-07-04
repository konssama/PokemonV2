from Api.RequestType import requestType

class Type:
    def __init__(self, type:str):
        self.name = type.title()
        self.response = requestType(type)

        self.doubleDamageFrom = []
        for i in self.response['damage_relations']['double_damage_from']:
            self.doubleDamageFrom.append(i['name'])

        self.doubleDamageTo = []
        for i in self.response['damage_relations']['double_damage_to']:
            self.doubleDamageTo.append(i['name'])

        self.halfDamageFrom = []
        for i in self.response['damage_relations']['half_damage_from']:
            self.halfDamageFrom.append(i['name'])

        self.halfDamageTo = []
        for i in self.response['damage_relations']['half_damage_to']:
            self.halfDamageTo.append(i['name'])

        self.noDamageFrom = []
        for i in self.response['damage_relations']['no_damage_from']:
            self.noDamageFrom.append(i['name'])

        self.noDamageTo = []
        for i in self.response['damage_relations']['no_damage_to']:
            self.noDamageTo.append(i['name'])

    def __str__(self) -> str:
        st = ""
        st += "Name: " + self.name + "\n"
        st += "Double Damage From: "
        for i in self.doubleDamageFrom: st += str(i) + ", "
        st += "\n"
        st += "Double Damage To: "
        for i in self.doubleDamageTo: st += str(i) + ", "
        st += "\n"
        st += "Half Damage From: "
        for i in self.halfDamageFrom: st += str(i) + ", "
        st += "\n"
        st += "Half Damage To: "
        for i in self.halfDamageTo: st += str(i) + ", "
        st += "\n"
        st += "No Damage From: "
        for i in self.noDamageFrom: st += str(i) + ", "
        st += "\n"
        st += "No Damage To: "
        for i in self.noDamageTo: st += str(i) + ", "
        st += "\n"

        st += "------------------------------------------------------------"
        
        return st