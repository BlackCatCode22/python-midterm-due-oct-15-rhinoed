# parser for arriving animals strings
# for python-midterm-program
# Mark Edmunds
# created October 10, 2023

import os
import random

animal_names = os.path.join(os.getcwd(), "animalNames.txt")


class AnimalData:

    @staticmethod
    def get_species(my_str):
        """Returns the species of the incoming animal"""
        # check if my_str is a string if not raise TypeError
        if type(my_str) != str:
            raise TypeError("my_str must be a string")
        # Split my_str using the character space
        words = my_str.split()
        # words is a list you iterate over it, access elements by index, etc.
        # try to ger the 5th element on exception return None
        try:
            return words[4]
        except IndexError:
            print(f"IndexError: {my_str} is not long enough")
            return None

    @staticmethod
    def get_age(sub_str):
        """Returns the age of the incoming animal"""
        try:
            return int(sub_str.split()[0])
        except TypeError:
            pass

    @staticmethod
    def get_origin(sub_str):
        """Returns the zoo of origin for the incoming animal"""
        substrings = sub_str.split(" ")
        try:
            substrings.remove("from")
        except IndexError as e:
            print(e)
        return " ".join(substrings).strip()

    @staticmethod
    def get_color(sub_str):
        """Returns color string of the incoming animal"""
        substrings = sub_str.split()
        try:
            substrings.remove("color")
        except ValueError:
            pass
        return " ".join(substrings).strip()

    @staticmethod
    def gen_birth_day(season_str):
        """Returns a date based on birth season of the incoming animal"""
        try:
            season = season_str.split()[2].strip()
        except IndexError as ie:
            print(f"index error: {ie}")
        match season:
            case "spring":
                birthday = "March 21"
            case "summer":
                birthday = "June 21"
            case "fall":
                birthday = "September 21"
            case "winter":
                birthday = "December 21"
            case _:
                birthday = "January 1"
        return birthday

    @staticmethod
    def get_weight(sub_str):
        """Returns the weight of the incoming animal"""
        try:
            return int(sub_str.split()[0].strip())
        except ValueError as ve:
            print(f"error converting weight to int: {ve}")
            return 0

    @staticmethod
    def get_sex(sub_str):
        """Yes, please yeah baby! Just kidding returns the sex of the animal"""
        try:
            return sub_str.split()[3].strip()
        except IndexError as ie:
            print(f"sex string split index error: {ie}")
            return "sex: unknown"

    # class method returns a random name based on species
    @staticmethod
    def gen_animal_name(species):
        """Returns a random name for the animal based on species"""
        try:
            with open(animal_names, "r") as names_file:
                lines = names_file.read().splitlines()
                match species:
                    case "Hyena":
                        names = lines[2].split(",")
                    case "Lion":
                        names = lines[6].split(",")
                    case "Bear":
                        names = lines[10].split(",")
                    case "Tiger":
                        names = lines[14].split(",")
                return random.sample(names, 1)[0].strip()
        except FileExistsError as e:
            print(f"error with file {e}")
