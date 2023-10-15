# main program function
# for python-midterm-program
# Mark Edmunds
# created October 13, 2023

from interface import get_menu
from Zoo import Zoo

def main():
    while True:
        print(get_menu())
        match input(f"\nMake a selection: "):
            case "1":
                Zoo.process_animals()
            case "2":
                if Zoo.zoo_not_empty():
                    Zoo.output_to_file()
                else:
                    print("The Zoo is empty process incoming animals")
            case "3":
                if len(Zoo.hyena_habitat) != 0:
                    for hyena in Zoo.hyena_habitat:
                        print(hyena)
                else:
                    print("The habitat is empty")
            case "4":
                if len(Zoo.lion_habitat) != 0:
                    for lion in Zoo.lion_habitat:
                        print(lion)
                else:
                    print("The habitat is empty")
            case "5":
                if len(Zoo.bear_habitat) != 0:
                    for bear in Zoo.bear_habitat:
                        print(bear)
                else:
                    print("The habitat is empty")
            case "6":
                if len(Zoo.tiger_habitat) != 0:
                    for tiger in Zoo.tiger_habitat:
                        print(tiger)
                else:
                    print("The habitat is empty")
            case "7":
                break
            case _:
                print("invalid selection")


if __name__ == "__main__":
    main()
