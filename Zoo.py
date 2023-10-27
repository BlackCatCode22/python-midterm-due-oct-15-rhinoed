# Zoo class
# for python-midterm-project
# Mark Edmunds
# created October 3, 2023


from datetime import datetime
import os
from Animal import Hyena, Lion, Bear, Tiger
from parse_animal_data import AnimalData

arriving_animals = os.path.join(os.getcwd(), "arrivingAnimals.txt")
zoo_population_report = os.path.join(os.getcwd(), "zooPopulationReport.txt")


class Zoo:
    hyena_habitat = []
    lion_habitat = []
    bear_habitat = []
    tiger_habitat = []
    today = datetime.today().strftime('%Y-%m-%d')

    @staticmethod
    def gen_zoo_habitat(animal):
        match animal.species:
            case "Hyena":
                if len(Zoo.hyena_habitat) == 4:
                    raise HabitatFullError
                else:
                    Zoo.hyena_habitat.append(animal)
                    Hyena.increment_num_in_zoo()
            case "Lion":
                if len(Zoo.lion_habitat) == 4:
                    raise HabitatFullError
                else:
                    Zoo.lion_habitat.append(animal)
                    Lion.increment_num_in_zoo()
            case "Bear":
                if len(Zoo.bear_habitat) == 4:
                    raise HabitatFullError
                else:
                    Zoo.bear_habitat.append(animal)
                    Bear.increment_num_in_zoo()
            case "Tiger":
                if len(Zoo.tiger_habitat) == 4:
                    raise HabitatFullError
                else:
                    Zoo.tiger_habitat.append(animal)
                    Tiger.increment_num_in_zoo()

    @staticmethod
    def output_to_file():
        """Outputs the zoo population to file"""
        hyena_strings = [hyena.__str__() + f" arrived {Zoo.today}" for hyena in Zoo.hyena_habitat]
        lion_strings = [lion.__str__() + f" arrived {Zoo.today}" for lion in Zoo.lion_habitat]
        bear_strings = [bear.__str__() + f" arrived {Zoo.today}" for bear in Zoo.bear_habitat]
        tiger_strings = [tiger.__str__() + f" arrived {Zoo.today}" for tiger in Zoo.tiger_habitat]
        try:
            with open(zoo_population_report, "a") as output_file:
                output_file.write(
                    f"Hyena Habitat:\n\n" +
                    f"\n".join(hyena_strings) + "\n\n" 
                    f"Lion Habitat:\n\n" +
                    f"\n".join(lion_strings) + "\n\n" 
                    f"Bear Habitat:\n\n" +
                    f"\n".join(bear_strings) + "\n\n" 
                    f"Lion Habitat:\n\n" +
                    f"\n".join(tiger_strings) + "\n\n"
                )
        except PermissionError as e:
            print(e)

        print("write complete")

    @staticmethod
    def process_animals():
        """Creates new animal based on string from text file"""
        try:
            with open(arriving_animals, "r") as input_file:
                for line in input_file.readlines():
                    substrings = line.split(",")
                    try:
                        species = AnimalData.get_species(substrings[0])
                    except ValueError:
                        print("not a valid string")
                    match species:
                        case "hyena":
                            new_animal = Hyena(substrings)
                        case "lion":
                            new_animal = Lion(substrings)
                        case "bear":
                            new_animal = Bear(substrings)
                        case "tiger":
                            new_animal = Tiger(substrings)
                        case _:
                            raise ValueError("unexpected value for species ")
                    try:
                        Zoo.gen_zoo_habitat(new_animal)
                    except HabitatFullError as he:
                        print(f"an error occurred: {he}")
                print("arriving animal processing complete")
        except FileExistsError as fe:
            print(f"error processing animals {fe}")

    @staticmethod
    def zoo_not_empty():
        """Boolean check used in main .py to allow/disallow output"""
        total_animals = len(Zoo.hyena_habitat) + len(Zoo.lion_habitat) + len(Zoo.bear_habitat) + len(Zoo.tiger_habitat)
        if total_animals != 0:
            return True
        else:
            return False


class HabitatFullError(Exception):
    """Custom exception for zoo habitat"""
    def __init__(self, message="Zoo Habitat is full no more animals can be added"):
        self.message = message
        super().__init__(self.message)
