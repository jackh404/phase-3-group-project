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
        scan_print(f'{planet.id}: {planet.name}')
def list_species():
    species = Species.get_all()
    for species in species :
        scan_print(f'{species.id}: {species.name}')
        
def list_civilizations():
    civs = Civilization.get_all()
    for civ in civs :
        scan_print(f'{civ.id}: {civ.name}')
        
def find_planet_by_type():
    type = input("Enter the type of planet: ")
    planet = Planet.find_by_type(type)
    print(planet) if planet else print(f"Planet {type} not found")

def find_planet_by_id():
    id_ = input("Enter the planet's id: ")
    planet = Planet.find_by_id(id_)
    print(planet) if planet else print(f"Planet {id_} not found")
    
    


    

    
    
    
    


def list_types(cls):
    for i, t in enumerate(cls.types):
        print(f"{i+1}. {t}")

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
    print()
    
def create_species():
    species = None
    name = None
    type = None
    description = None
    home_world_id = None
    while(not species):
        if not name: name = input("Enter the name of the new species: ")
        print()
        scan_print("Available species types:")
        list_types(Species)
        print()
        if not type: type = input("Enter the type number of the new species: ")
        type = Species.types[int(type)-1]
        if not description: description = input("Enter the description of the new species: ")
        print()
        scan_print("Available planets:")
        list_planets()
        print()
        if not home_world_id: home_world_id = input("Enter the home world ID of the new species: ")
        try:
            species = Species.create(name, type, description, int(home_world_id))
            scan_print(f"Species {name} created successfully!\n{species}")
        except Exception as e:
            scan_print(f"Error: {e}")
            if input("Try again? (y/n): ") == "n":
                break
            else:
                if "Name" in e.__str__(): name = None
                elif "Type" in e.__str__(): type = None
                elif "Description" in e.__str__(): description = None
                elif "Home World" in e.__str__(): home_world_id = None
                species = None
    print()
    input("Press Enter to return to menu")
    print()

def create_civilization():
    civ = None
    name = None
    type = None
    description = None
    religions = None
    languages = None
    species_ids = []
    planet_ids = []
    while(not civ):
        if not name: name = input("Enter the name of the new civilization: ")
        print()
        scan_print("Available civilization types:")
        list_types(Civilization)
        print()
        if not type: type = input("Enter the type number of the new civilization: ")
        type = Civilization.types[int(type)-1]
        if not description: description = input("Enter the description of the new civilization: ")
        if not religions: religions = input("Enter the major religions of the new civilization separated by commas: ")
        if not languages: languages = input("Enter the major languages of the new civilization separated by commas: ")
        if not species_ids: 
            while True:
                print()
                scan_print("Available Species:")
                list_species()
                print()
                id_ = input("Enter the ID of a species in the new civilization or press Enter to continue: ")
                if id_:
                    id_ = int(id_)
                    if id_ not in species_ids:
                        species_ids.append(id_)
                else:
                    break
        if not planet_ids: 
            while True:
                print()
                scan_print("Available Planets:")
                list_planets()
                print()
                id_ = input("Enter the ID of a planet in the new civilization or press Enter to continue: ")
                if id_:
                    id_ = int(id_)
                    if id_ not in planet_ids:
                        planet_ids.append(id_)
                else:
                    break
        try:
            civ = Civilization.create(name, type, description, religions, languages, species_ids, planet_ids)
            scan_print(f"Civilization {name} created successfully!\n{civ}")
        except Exception as e:
            scan_print(f"Error: {e}")
            if input("Try again? (y/n): ") == "n":
                break
            else:
                if "Name" in e.__str__(): name = None
                elif "Type" in e.__str__(): type = None
                elif "Description" in e.__str__(): description = None
                elif "Religions" in e.__str__(): religions = None
                elif "Languages" in e.__str__(): languages = None
                elif "Species" in e.__str__(): species_ids = []
                elif "Planets" in e.__str__(): planet_ids = []
                civ = None
                
    print()
    input("Press Enter to return to menu")
    print()
    
def update_civilization():
    list_civilizations()
    id_ = input("Enter the civilization's id: ")
    try:
        if civ := Civilization.find_by_id(int(id_)):
            print(civ)
            ans = input("Change the civilization's name? (y/n): ")
            if "y" in ans.lower():
                name = input("Enter the civilizations's new name: ")
                civ.name = name
            ans = input("Change the civilizations's type? (y/n): ")
            if "y" in ans.lower():
                print()
                scan_print("Available civilization types:")
                list_types(Civilization)
                print()
                input("Enter the new type number for the civilization: ")
                type = Civilization.types[int(type)-1]
                civ.type = type
            ans = input("Change the civilizations's description? (y/n): ")
            if "y" in ans.lower():
                description = input("Enter the new description: ")
                civ.description = description
            ans = input("Change the civilizations's major religions? (y/n): ")
            if "y" in ans.lower():
                religions = input("Enter the new major religions separated by commas: ")
                civ.religions = religions
            ans = input("Change the civilizations's major languages? (y/n): ")
            if "y" in ans.lower():
                languages = input("Enter the new major languages separated by commas: ")
                civ.languages = languages
            ans = input("Change the civilizations's species? You will need to enter the ID of each species again. (y/n): ")
            if "y" in ans.lower():
                civ.species_ids = []
                while True:
                    print()
                    scan_print("Available Species:")
                    list_species()
                    print()
                    id_ = input("Enter the ID of a species in the civilization or press Enter to continue: ")
                    if id_:
                        id_ = int(id_)
                        if id_ not in civ.species_ids:
                            civ.species_ids.append(id_)
                    else:
                        break
            ans = input("Change the civilizations's planets? You will need to enter the ID of each planet again. (y/n): ")
            if "y" in ans.lower():
                civ.species_ids = []
                while True:
                    print()
                    scan_print("Available Planets:")
                    list_planets()
                    print()
                    id_ = input("Enter the ID of a planet in the civilization or press Enter to continue: ")
                    if id_:
                        id_ = int(id_)
                        if id_ not in civ.planet_ids:
                            civ.planet_ids.append(id_)
                    else:
                        break
            civ.update()
            scan_print(f"Civilization {civ.name} updated successfully!\n{civ}")
        else:
            print(f"Civilization {id_} not found")
    except Exception as exc:
        print("Error updating: ", exc)
    print()
    input("Press Enter to return to menu")
    print()