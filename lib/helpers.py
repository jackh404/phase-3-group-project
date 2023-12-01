# lib/helpers.py
from models.planet import Planet
from models.star import Star
from models.species import Species
from models.civilization import Civilization
from time import sleep
from sys import stdout

# def helper_1():
#     print("Performing useful function#1.")


def exit_program():
    print("Exit program!")
    exit()

def scan_print(s,t=0.01):
    for c in s:
        stdout.write(c)
        stdout.flush()
        sleep(t)
    print()
    
def initialize_from_database():
    Star.get_all()
    Planet.get_all()
    Species.get_all()
    Civilization.get_all()
    
def list_stars():
    stars = Star.get_all()
    for star in stars:
        scan_print(f'{star.id}: {star.name}')

def find_star_by_type():
    type = input("Enter the star type:")
    star = Star.find_by_type(type)
    print(star) if star else print(f"Star {type} not found")

def list_types(cls):
    for i, t in enumerate(cls.types):
        scan_print(f'{i+1}: {t}')


def create_planet():
    planet = None
    pname = None
    ptype = None
    pdescription = None
    pdiameter = None
    pmass = None
    pday = None
    pyear = None
    pstar = None
    while(not planet):
        if not pname: pname = input("Enter the name of the new planet: ")
        print()
        scan_print("Available planet types:")
        list_types(Planet)
        print()
        if not ptype: ptype = input("Enter the type number of the new planet: ")
        ptype = Planet.types[int(ptype)-1]
        if not pdescription: pdescription = input("Enter the description of the new planet: ")
        if not pdiameter: pdiameter = input("Enter the diameter of the new planet in kilometers: ")
        if not pmass: pmass = input("Enter the mass of the new planet in trillions of kilograms: ")
        if not pday: pday = input("Enter the day length of the new planet in Earth days: ")
        if not pyear: pyear = input("Enter the year length of the new planet in Earth years: ")
        print()
        scan_print("Available stars:")
        list_stars()
        print()
        pstar = input("Enter the star ID of the new planet: ")
        try:
            planet = Planet.create(pname, ptype, pdescription, pdiameter, pmass, pday, pyear, int(pstar))
            scan_print(f"Planet {pname} created successfully!\n{planet}")
        except Exception as e:
            scan_print(f"Error: {e}")
            if input("Try again? (y/n): ") == "n":
                break
            else:
                if "Name" in e.__str__(): pname = None
                elif "Type" in e.__str__(): ptype = None
                elif "Description" in e.__str__(): pdescription = None
                elif "Diameter" in e.__str__(): pdiameter = None
                elif "Mass" in e.__str__(): pmass = None
                elif "Day" in e.__str__(): pday = None
                elif "Year" in e.__str__(): pyear = None
                elif "Star" in e.__str__(): pstar = None
                planet = None
    print()
    input("Press Enter to return to menu")