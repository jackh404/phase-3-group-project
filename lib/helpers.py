# lib/helpers.py
from models.planet import Planet
from models.star import Star
from models.species import Species
from models.civilization import Civilization
from time import sleep
from sys import stdout

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
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