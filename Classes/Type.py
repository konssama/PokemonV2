from Api.RequestType import requestType

class Type:
    def __init__(self, type) -> None:
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