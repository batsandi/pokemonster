import random


class TypesMatrixMixin():
    __poke_types_list = [
        "normal",
        "fire",
        "water",
        "electric",
        "grass",
        "ice",
        "fighting",
        "poison",
        "ground",
        "flying",
        "psychic",
        "bug",
        "rock",
        "ghost",
        "dragon",
        "dark",
        "steel",
        "fairy",
    ]

    __factors_list_of_lists = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 / 2, 0, 1, 1, 1 / 2, 1],
        [1, 1 / 2, 1 / 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1 / 2, 1, 1 / 2, 1, 2, 1],
        [1, 2, 1 / 2, 1, 1 / 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1 / 2, 1, 1, 1],
        [1, 1, 2, 1 / 2, 1 / 2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1 / 2, 1, 1, 1],
        [1, 1 / 2, 2, 1, 1 / 2, 1, 1, 1 / 2, 2, 1 / 2, 1, 1 / 2, 2, 1, 1 / 2, 1, 1 / 2, 1],
        [1, 1 / 2, 1 / 2, 1, 2, 1 / 2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1 / 2, 1],
        [2, 1, 1, 1, 1, 2, 1, 1 / 2, 1, 1 / 2, 1 / 2, 1 / 2, 2, 0, 1, 2, 2, 1 / 2],
        [1, 1, 1, 1, 2, 1, 1, 1 / 2, 1 / 2, 1, 1, 1, 1 / 2, 1 / 2, 1, 1, 0, 2],
        [1, 2, 1, 2, 1 / 2, 1, 1, 2, 1, 0, 1, 1 / 2, 2, 1, 1, 1, 2, 1],
        [1, 1, 1, 1 / 2, 2, 1, 2, 1, 1, 1, 1, 2, 1 / 2, 1, 1, 1, 1 / 2, 1],
        [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1 / 2, 1, 1, 1, 1, 0, 1 / 2, 1],
        [1, 1 / 2, 1, 1, 2, 1, 1 / 2, 1 / 2, 1, 1 / 2, 2, 1, 1, 1 / 2, 1, 2, 1 / 2, 1 / 2],
        [1, 2, 1, 1, 1, 2, 1 / 2, 1, 1 / 2, 2, 1, 2, 1, 1, 1, 1, 1 / 2, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1 / 2, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1 / 2, 0],
        [1, 1, 1, 1, 1, 1, 1 / 2, 1, 1, 1, 2, 1, 1, 2, 1, 1 / 2, 1, 1 / 2],
        [1, 1 / 2, 1 / 2, 1 / 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1 / 2, 2],
        [1, 1 / 2, 1, 1, 1, 1, 2, 1 / 2, 1, 1, 1, 1, 1, 1, 2, 2, 1 / 2, 1]
    ]

    #     The below code does not work because of an issue with the scope of nested comprehensions within Classes not accessing class attributes.
    #     Hence, I have re-written it as a dict comprehension -> for loop -> assign to protected variable to be available in inheritence
    #     See below for more info:
    #     https://stackoverflow.com/questions/36161632/python-nested-dictionary-comprehension-in-static-class-scope-variable-not-defin
    #
    #     _types_factors_dict = {poke_type: {poke_type: factor for (poke_type, factor) in zip(__poke_types_list, factors_list)}
    #                                for (poke_type, factors_list)
    #                                in zip(__poke_types_list, __factors_list_of_lists)
    #                          }

    __types_factors_dict = {poke_type: factors_list
                            for (poke_type, factors_list)
                            in zip(__poke_types_list, __factors_list_of_lists)
                            }

    for key, value in __types_factors_dict.items():
        __types_factors_dict[key] = {poke_type: factor
                                     for (poke_type, factor)
                                     in zip(__poke_types_list, value)
                                     }

    _types_factors_dict = __types_factors_dict


class Battle(TypesMatrixMixin):
    fighters_list = []
    attacker = None
    defender = None
    current_round = 0
    winner = None
    fight_log = []

    @classmethod
    def assign_roles(cls, pokemon_1, pokemon_2):
        if cls.current_round == 0:
            cls.fighters_list = sorted(
                [pokemon_1, pokemon_2],
                key=lambda x: x.speed,
            )

        cls.attacker = cls.fighters_list.pop()
        cls.defender = cls.fighters_list.pop()
        cls.fighters_list = [cls.attacker, cls.defender]
        return cls.attacker, cls.defender

    @classmethod
    def attack(cls, attacker, defender):
        critical = False
        attacker_type = cls.attacker.types[random.randint(0, len(cls.attacker.types) - 1)]
        defender_type = cls.defender.types[random.randint(0, len(cls.defender.types) - 1)]
        type_factor = cls._types_factors_dict[attacker_type][defender_type]

        damage = 10
        damage *= (cls.attacker.attack / cls.defender.defense)
        damage *= type_factor
        damage *= random.uniform(0.7, 1)
        if random.randint(0, 100) > 95:
            critical = True
            damage *= 2

        damage = round(damage)
        cls.defender.hp -= damage

        return attacker_type, defender_type, type_factor, damage, critical

    @classmethod
    def fight(cls, pokemon_1, pokemon_2):
        cls.fight_log = []
        while pokemon_1.hp > 0 and pokemon_2.hp > 0:

            cls.attacker, cls.defender = cls.assign_roles(pokemon_1, pokemon_2)
            cls.current_round += 1
            attacker_type, defender_type, type_factor, damage, critical = cls.attack(cls.attacker, cls.defender)
            if critical:
                cls.fight_log.append(
                    f"{cls.attacker} dealt {damage} (x{type_factor} {attacker_type.title()} vs. {defender_type.title()}) CRITICAL to {cls.defender} - HP: {cls.defender.hp}^")

            else:
                cls.fight_log.append(
                    f"{cls.attacker} dealt {damage} (x{type_factor} {attacker_type.title()} vs. {defender_type.title()}) damage to {cls.defender} - HP: {cls.defender.hp}^")

        cls.current_round = 0
        winner = cls.attacker
        return winner, ', '.join(cls.fight_log)


class PokemonFromAPI:
    DM_TO_CM = 10

    def __init__(self, pokemon_json):
        self.id = pokemon_json['id']
        self.name = pokemon_json['name']
        self.image = pokemon_json['sprites']['other']['official-artwork']['front_default']
        self.height = pokemon_json['height'] * self.DM_TO_CM
        self.weight = pokemon_json['weight']
        self.types = [type['type']['name'] for type in pokemon_json['types']]
        self.__stats = pokemon_json['stats']
        self.hp = self.__stats[0]['base_stat']

    @property
    def attack(self):
        return self.__stats[1]['base_stat']

    @property
    def defense(self):
        return self.__stats[2]['base_stat']

    @property
    def speed(self):
        return self.__stats[5]['base_stat']

    def get_data_for_model(self):
        data = {
            'name': self.name,
            'image': self.image,
            'types': self.types,
            'hp': self.hp,
            'attack': self.attack,
            'defense': self.defense,
            'speed': self.speed,
        }

        return data

    def __str__(self):
        return self.name.title()


