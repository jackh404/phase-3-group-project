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