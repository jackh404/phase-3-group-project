# lib/helpers.py 
from models.planet import Planet
from models.star import Star
from models.species import Species
from models.civilization import Civilization
from time import sleep
from sys import stdout

title_string = """
  _______      ___       __           ___        ______ .___________. __    ______         ___      .___________. __           ___           _______.
 /  _____|    /   \     |  |         /   \      /      ||           ||  |  /      |       /   \     |           ||  |         /   \         /       |
|  |  __     /  ^  \    |  |        /  ^  \    |  ,----'`---|  |----`|  | |  ,----'      /  ^  \    `---|  |----`|  |        /  ^  \       |   (----`
|  | |_ |   /  /_\  \   |  |       /  /_\  \   |  |         |  |     |  | |  |          /  /_\  \       |  |     |  |       /  /_\  \       \   \    
|  |__| |  /  _____  \  |  `----. /  _____  \  |  `----.    |  |     |  | |  `----.    /  _____  \      |  |     |  `----. /  _____  \  .----)   |   
 \______| /__/     \__\ |_______|/__/     \__\  \______|    |__|     |__|  \______|   /__/     \__\     |__|     |_______|/__/     \__\ |_______/    
                                                                                                                                                                                                                                                                               
"""
title_array = ["  _______      ___       __           ___        ______ .___________. __    ______         ___      .___________. __           ___           _______.",
               " /  _____|    /   \     |  |         /   \      /      ||           ||  |  /      |       /   \     |           ||  |         /   \         /       |",
               "|  |  __     /  ^  \    |  |        /  ^  \    |  ,----'`---|  |----`|  | |  ,----'      /  ^  \    `---|  |----`|  |        /  ^  \       |   (----`",
               "|  | |_ |   /  /_\  \   |  |       /  /_\  \   |  |         |  |     |  | |  |          /  /_\  \       |  |     |  |       /  /_\  \       \   \    ",
               "|  |__| |  /  _____  \  |  `----. /  _____  \  |  `----.    |  |     |  | |  `----.    /  _____  \      |  |     |  `----. /  _____  \  .----)   |   ",
               " \______| /__/     \__\ |_______|/__/     \__\  \______|    |__|     |__|  \______|   /__/     \__\     |__|     |_______|/__/     \__\ |_______/    "]

def intro():
    scan_print("Welcome to the...",0.1)
    for line in title_array:
        scan_print(line,0.002)
    print()
    scan_print("Press Enter to continue")
    input()


def exit_program():
    scan_print("Exit the Astral Plane!")
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

def find_star_by_id():
    id_ = input("Enter the star's id: ")
    star = Star.find_by_id(int(id_))
    scan_print(f'{star}') if star else print(f" Star {id_} not found")

def create_star():
    star = None
    sname = None
    stype = None
    sdescription = None
    sdiameter = None
    smass = None
    while(not star):
        if not sname: sname = input("Enter the name of the new star: ")
        print()
        scan_print("Available star types: ")
        list_types(Star)
        print()
        if not stype: stype = input("Enter the type number of the new star: ")
        stype = Star.types[int(stype)-1]
        if not sdescription: sdescription = input("Enter the description of the new star: ")
        if not sdiameter: sdiameter = input("Enter the diameter of the new star in kilometers: ")
        if not smass: smass = input("Enter the mass of the new planet in trillions of kilograms: ")
        try:
            star = Star.create(sname,stype,sdescription,sdiameter,smass)
            scan_print(f"Star {star.name} created successfully!\n{star}")
        except Exception as e:
            scan_print(f"Error: {e}")
            if input("Try again? (y/n): ") =="n": 
                break
            else:
                if "Name" in e._str_(): sname = None
                elif "Type" in e._str_():stype = None
                elif "Description" in e._str_(): sdescription = None
                elif "Diameter" in e._str_(): sdiameter = None
                elif "Smass" in e._str_(): smass = None
                star = None
    print()
    input("Press Enter to return to menu")
                

def update_star():

    id_ = input("Enter the star's id: ")
    id_ = int(id_)
    if star := Star.find_by_id(id_):
        scan_print(f'{star}')
        try:
            ans = input("Change the star's name? (y/n): ")
            if "y" in ans.lower():
                name = input("Enter the star's new name: ")
                star.name = name 
            ans = input("Change the star type? (y/n): ")
            if "y" in ans.lower():
                print()
                scan_print("Available star types:")
                list_types(Star)
                print()
                typ = input("Enter the new type number for the star: ")
                type = Star.types[int(typ)-1]
                star.type = type
            ans = input("Change the star's description? (y/n): ")
            if "y" in ans.lower():
                description = input("Enter the star's new description: ")
                star.description = description
            ans = input("Change the star's diameter? (y/n): ")
            if "y" in ans.lower(): 
                diameter = input("Enter the new diameter in kilometers: ")
                star.diameter = diameter
            ans = input("Change the star's mass? (y/n): ")
            if "y" in ans.lower(): 
                mass = input("Enter the new mass in trillions of kilograms: ")
                star.mass = mass
            star.update()
            scan_print("Unleashing the star...from the dust")
            scan_print("...\n",0.5)
            scan_print(f"Star {name} added to star system!\n{star}")
        except Exception as e: 
            scan_print(f"Error: {e}")
            print()
            input("Press Enter to return to menu")
            print()
                
            type = input("Enter the new star type: ")
            star.type = type
            
            star.update()
            scan_print(f"BORN FROM THE ASHES:{star}")
        except Exception as exc:
            scan_print("Error updating: ", exc)
    else:
        scan_print("...",0.5)
        scan_print(f" Star {id_} not found")
    print()
    input("Press Enter to return to menu")
    print()
    
def delete_star():
    id_ = input("Enter the star's id: ")
    try:
        id_ = int(id_)
    except:
        scan_print("Error: Star ID must be an integer")
        print()
        input("Press Enter to return to menu")
        print()
        return
    if star := Star.find_by_id(id_) :
        scan_print(f'Delete star: {star.name}? (y/n): ')
        if "y" in input():
            star.delete()
            scan_print("Deploying black hole")
            scan_print("...\n",0.5)
            scan_print(f"Star {id_} deleted")
    else:
        scan_print("...",0.5)
        scan_print(f"Star {id_} not found")
    print()
    input("Press Enter to return to menu")
    print()

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
    print()
    scan_print("Available planet types:")
    list_types(Planet)
    print()
    typ = input("Enter the type number to search: ")
    type = Planet.types[int(typ)-1]
    planets = Planet.find_by_type(type)
    if planets:
        scan_print(f"Planets of type '{type}':")
        for planet in planets :
            scan_print(f'{planet.id}: {planet.name}')
    else:
        print(f"No planets of type {type} found")
    print()
    input("Press Enter to return to menu")
    print()

def find_planet_by_id():
    id_ = input("Enter the planet's id: ")
    planet = Planet.find_by_id(id_)
    print(planet) if planet else print(f"Planet {id_} not found")
    print()
    input("Press Enter to return to menu")
    print()
    
def list_types(cls):
    for i, t in enumerate(cls.types):
        print(f"{i+1}. {t}")

def create_planet():
    planet = None
    name = None
    type = None
    description = None
    diameter = None
    mass = None
    day = None
    year = None
    star = None
    while(not planet):
        if not name: name = input("Enter the name of the new planet: ")
        print()
        scan_print("Available planet types:")
        list_types(Planet)
        print()
        if not type: ptype = input("Enter the type number of the new planet: ")
        type = Planet.types[int(ptype)-1]
        if not description: description = input("Enter the description of the new planet: ")
        if not diameter: diameter = input("Enter the diameter of the new planet in kilometers: ")
        if not mass: mass = input("Enter the mass of the new planet in trillions of kilograms: ")
        if not day: day = input("Enter the day length of the new planet in Earth days: ")
        if not year: year = input("Enter the year length of the new planet in Earth years: ")
        print()
        scan_print("Available stars:")
        list_stars()
        print()
        star = input("Enter the star ID of the new planet: ")
        try:
            planet = Planet.create(name, type, description, diameter, mass, day, year, int(star))
            scan_print(f"Planet {name} created successfully!\n{planet}")
        except Exception as e:
            scan_print(f"Error: {e}")
            if input("Try again? (y/n): ") == "n":
                break
            else:
                if "Name" in e.__str__(): name = None
                elif "Type" in e.__str__(): type = None
                elif "Description" in e.__str__(): description = None
                elif "Diameter" in e.__str__(): diameter = None
                elif "Mass" in e.__str__(): mass = None
                elif "Day" in e.__str__(): day = None
                elif "Year" in e.__str__(): year = None
                elif "Star" in e.__str__(): star = None
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
            scan_print("Deploying memetic rewrite")
            scan_print("...\n",0.5)
            scan_print(f"Civilization {civ.name} updated successfully!\n{civ}")
        else:
            print(f"Civilization {id_} not found")
    except Exception as exc:
        print("Error updating: ", exc)
    print()
    input("Press Enter to return to menu")
    print()
    
def delete_civilization():
    list_civilizations()
    id_ = input("Enter the civilization's id: ")
    if civ := Civilization.find_by_id(int(id_)):
        civ.delete()
        scan_print("Deploying colonizers")
        scan_print("...\n",0.5)
        scan_print(f"Civilization {id_} deleted")
    else:
        scan_print("...",0.5)
        scan_print(f"Civilization {id_} not found")
    print()
    input("Press Enter to return to menu")
    print()
    
def find_civilization_by_name():
    name = input("Enter the name of the civilization: ")
    if civ := Civilization.find_by_name(name):
        scan_print(civ)
    else:
        scan_print("...",0.5)
        scan_print(f"Civilization {name} not found")
    print()
    input("Press Enter to return to menu")
    print()
    
def find_civilization_by_type():
    print()
    scan_print("Available civilization types:")
    list_types(Civilization)
    print()
    input("Enter the new type number for the civilization: ")
    type = Civilization.types[int(type)-1]
    if civs := Civilization.find_by_type(type):
        for civ in civs:
            scan_print(civ)
    else:
        scan_print("...",0.5)
        scan_print(f"No civilizations of type {type} found")
    print()
    input("Press Enter to return to menu")
    print()
    
def find_civilization_by_id():
    id_ = input("Enter the civilization's id: ")
    if civ := Civilization.find_by_id(int(id_)):
        scan_print(civ)
    else:
        scan_print("...",0.5)
        scan_print(f"Civilization {id_} not found")
    print()
    input("Press Enter to return to menu")
    print()
    
def update_planet():
    list_planets()
    id_ = input("Enter the planet's id: ")
    if planet := Planet.find_by_id(int(id_)):
        try:
            ans = input("Change the planet's name? (y/n): ")
            if "y" in ans.lower():
                name = input("Enter the new name: ")
                planet.name = name
            ans = input("Change the planet's type? (y/n): ")
            if "y" in ans.lower():
                print()
                scan_print("Available planet types:")
                list_types(Planet)
                print()
                input("Enter the new type number for the planet: ")
                type = Planet.types[int(type)-1]
                planet.type = type
            ans = input("Change the planet's description? (y/n): ")
            if "y" in ans.lower():
                description = input("Enter the new description: ")
                planet.description = description
            ans = input("Change the planet's diameter? (y/n):")
            if "y" in ans.lower():
                diameter = input("Enter the new diameter in kilometers: ")
                planet.diameter = diameter
            ans = input("Change the planet's mass? (y/n): ")
            if "y" in ans.lower():
                mass = input("Enter the new mass in trillions of kilograms: ")
                planet.mass = mass
            ans = input("Change the planet's day length? (y/n): ")
            if "y" in ans.lower():
                day = input("Enter the new day length in Earth days: ")
                planet.day = day
            ans = input("Change the planet's year length? (y/n): ")
            if "y" in ans.lower():
                year = input("Enter the new year length in Earth years: ")
                planet.year = year
            planet.update()
            scan_print("Deploying terraforming platforms")
            scan_print("...\n",0.5)
            scan_print(f"Planet {name} updated successfully!\n{planet}")
        except Exception as e:
            scan_print(f"Error: {e}")  
        print()
        input("Press Enter to return to menu")
        print()
        
def delete_planet():
    list_planets()
    id_ = input("Enter the planet's id: ")
    if planet := Planet.find_by_id(int(id_)):
        planet.delete()
        scan_print("Deploying cosmic devourers")
        scan_print("...\n",0.5)
        scan_print(f"Planet {id_} deleted")
    else:
        scan_print("...",0.5)
        scan_print(f"Planet {id_} not found")
    print()
    input("Press Enter to return to menu")
    print()
    
def find_species_by_id():
    id_ = input("Enter the species's id: ")
    if species := Species.find_by_id(int(id_)):
        scan_print(f'{species}')
    else:
        scan_print("...",0.5)
        scan_print(f"Species {id_} not found")
    print()
    input("Press Enter to return to menu")
    print()

def find_species_by_name():
    name = input("Enter the species's name: ")
    if species := Species.find_by_name(name):
        scan_print(species)
    else:
        scan_print("...",0.5)
        scan_print(f"Species {name} not found")
    print()
    input("Press Enter to return to menu")
    print()
    
def find_species_by_type():
    print()
    scan_print("Available species types:")
    list_types(Species)
    print()
    input("Enter the new type number for the species: ")
    type = Species.types[int(type)-1]
    if species := Species.find_by_type(type):
        for spec in species:
            scan_print(spec)
    else:
        scan_print("...",0.5)
        scan_print(f"No species of type {type} found")
    print()
    input("Press Enter to return to menu")
    print()
    
def update_species():
    list_species()
    id_ = input("Enter the species's id: ")
    if species := Species.find_by_id(int(id_)):
        try:
            ans = input("Change the species's name? (y/n): ")
            if "y" in ans.lower():
                name = input("Enter the new name: ")
                species.name = name
            ans = input("Change the species's type? (y/n): ")
            if "y" in ans.lower():
                print()
                scan_print("Available species types:")
                list_types(Species)
                print()
                type = input("Enter the new type number for the species: ")
                type = Species.types[int(type)-1]
                species.type = type
            ans = input("Change the species's description? (y/n): ")
            if "y" in ans.lower():
                description = input("Enter the new description: ")
                species.description = description
            ans = input("Change the species's home world? (y/n): ")
            if "y" in ans.lower():
                print()
                scan_print("Available worlds:")
                list_planets()
                print()
                home_world_id = input("Enter the new home world ID: ")
                species.home_world_id = home_world_id
            species.update()
            scan_print("Deploying CRISPR viruses")
            scan_print("...\n",0.5)
            scan_print(f"Species {name} updated successfully!\n{species}")
        except Exception as e:
            scan_print(f"Error: {e}")  
        print()
        input("Press Enter to return to menu")
        print()
        
def delete_species():
    list_species()
    id_ = input("Enter the species's id: ")
    if species := Species.find_by_id(int(id_)):
        species.delete()
        scan_print("Deploying Genophage")
        scan_print("...\n",0.5)
        scan_print(f"Species {id_} deleted")
    else:
        scan_print("...",0.5)
        scan_print(f"Species {id_} not found")
    print()
    input("Press Enter to return to menu")
    print()