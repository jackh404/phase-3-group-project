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
        print(star)

def find_star_by_type():
    type = input("Enter the star type:")
    star = Star.find_by_type(type)
    print(star) if star else print(f"Star {type} not found")

def find




def create_planet():
    pname = input("Enter the name of the new planet: ")
    ptype = input("Enter the type of the new planet: ")
    pdescription = input("Enter the description of the new planet: ")
    pdiameter = input("Enter the diameter of the new planet in kilometers:")
    