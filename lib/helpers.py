# lib/helpers.py
from models.planet import Planet
from models.star import Star
from models.species import Species
from models.civilization import Civilization
from time import sleep
from sys import stdout




def exit_program():
    print("Exit the Astral Plane!")
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
    for stars in stars:
        scan_print(stars)

def find_star_by_type():
    type = input("Enter the star type:")
    star = Star.find_by_type(type)
    print(star) if star else print(f"Star {type} not found")

def find_star_by_id():
    id_ = input("Enter the star's id: ")
    star = Star.find_by_id(id_)
    print(star) if star else print(f" Star {id_} not found")

def create_star():
    name = input("Enter the star's name: ")
    type = input("Enter the star type: ")
    id_ = input("Enter the star's id: ")
    try :
        department = Star.create(name, type, id_)
    except Exception as exc: 
        print("SWALLOWED BY BLACKHOLE:", exc)

def update_star():
    id_ = input("Enter the star's id: ")
    if star := Star.find_by_id(id_):
        try:
            name = input("Enter the star's new name: ")
            star.name = name 
            type = input("Enter the new star type: ")
            star.type = type
            
            star.update()
            print(f"BORN FROM THE ASHES:{star}")
        except Exception as exc:
            print("Error updating: ", exc)
    else: 
        print(f" Star {id_} not found")
    
def delete_star():
    id_ = input("Enter the star's id: ")
    if star := Star.find_by_id(id_) :
        star.delete()
        print(f"Star {id_} deleted")
    else:
        print(f"Star {id_} not found")

def list_planets():
    planets = Planet.get_all()
    for planet in planets :
        print(planet)
        
def find_planet_by_type():
    type = input("Enter the type of planet: ")
    planet = Planet.find_by_type(type)
    print(planet) if planet else print(f"Planet {type} not found")

def find_planet_by_id():
    id_ = input("Enter the planet's id: ")
    planet = Planet.find_by_id(id_)
    print(planet) if planet else print(f"Planet {id_} not found")
    
    


    

    
    
    
    




def create_planet():
    pname = input("Enter the name of the new planet: ")
    ptype = input("Enter the type of the new planet: ")
    pdescription = input("Enter the description of the new planet: ")
    pdiameter = input("Enter the diameter of the new planet in kilometers:")
    