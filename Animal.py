# Animal class and subclasses
# for python-midterm-program
# Mark Edmunds
# created September 28, 2023


from abc import ABC
from datetime import datetime
from parse_animal_data import AnimalData


def format_date_str(birth_day, year):
    time_string = datetime.strptime(f"{birth_day}, {year}", "%B %d, %Y")
    return time_string.strftime('%Y-%m-%d')


# Animal class definition
class Animal(ABC):
    """Class in not meant to be instantiated directly but can be subclassed"""

    def __init__(self, info_strings, species):
        self.id = self.gen_unique_animal_id()
        self.species = species
        self.name = AnimalData.gen_animal_name(self.species)
        self.birth_day = AnimalData.gen_birth_day(info_strings[1])
        try:
            self.age = int(AnimalData.get_age(info_strings[0]))
            self.birth_year = datetime.now().year - self.age
            self.birth_string = format_date_str(self.birth_day, self.birth_year)
        except ValueError as ve:
            print(f"cannot convert to integer {ve}")
        self.color = AnimalData.get_color(info_strings[2])
        self.weight = AnimalData.get_weight(info_strings[3])
        self.sex = AnimalData.get_sex(info_strings[0])
        self.zoo_of_origin = AnimalData.get_origin(info_strings[4])
        self.zoo_local = info_strings[5].strip()

    def some_method(self):
        pass

    # class str method returns string describing class instance
    def __str__(self):
        try:
            return (f"{self.id}, {self.name}, "
                    f"{self.age} years old, birthdate {self.birth_string}, "
                    f"{self.color} color, {self.sex}, {self.weight} pounds, from "
                    f"{self.zoo_of_origin}, {self.zoo_local}")
        except AttributeError as ae:
            print(f"class missing attribute: {ae}")
            return (f"{self.id}, {self.name}, {self.color} color, "
                    f"{self.sex}, {self.weight}, from {self.zoo_of_origin}, "
                    f"{self.zoo_local}")

    @classmethod
    def get_num_in_zoo(cls):
        """Returns the number of a species int the zoo"""
        return cls.NUM_IN_ZOO

    # class method generating unique id
    @classmethod
    def gen_unique_animal_id(cls):
        """Returns a unique id"""
        return f"{cls.SPECIES[0:2]}{cls.NUM_IN_ZOO + 1:02}"

    @classmethod
    def increment_num_in_zoo(cls):
        cls.NUM_IN_ZOO += 1


# Hyena subclass
class Hyena(Animal):
    SPECIES = "Hyena"
    NUM_IN_ZOO = 0

    def __init__(self, info_strings):
        super().__init__(info_strings, Hyena.SPECIES)

    def cackle(self, animal):
        print(f"The hyena {self.name} cackles at the {animal}")


# Lion subclass
class Lion(Animal):
    SPECIES = "Lion"
    NUM_IN_ZOO = 0

    def __init__(self, info_strings):
        super().__init__(info_strings, Lion.SPECIES)


# Bear subclass
class Bear(Animal):
    SPECIES = "Bear"
    NUM_IN_ZOO = 0

    def __init__(self, info_strings):
        super().__init__(info_strings, Bear.SPECIES)

    def hibernate(self, duration):
        print(f"{self.name} the bear will hibernate for {duration} days")


# Tiger subclass
class Tiger(Animal):
    SPECIES = "Tiger"
    NUM_IN_ZOO = 0

    def __init__(self, info_strings):
        super().__init__(info_strings, Tiger.SPECIES)
