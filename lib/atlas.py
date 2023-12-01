#!/usr/bin/env python3
#lib/atlas.py
from helpers import (
    exit_program,
    list_stars,
    find_star_by_type,
    find_star_by_id,
    create_star,
    update_star,
    delete_star,
    list_planets,
    find_planet_by_type,
    find_planet_by_id,
    create_planet,
    update_planet,
    delete_planet,
    list_civilizations,
    find_civilization_by_type,
    find_civilization_by_id,
    create_civilization,
    update_civilization,
    delete_civilization,
    list_species,
    find_species_by_type,
    find_species_by_id,
    create_species,
    update_species,
    delete_species,
    intro,
    scan_print
)
    
def main():
    intro()
    while True:
        top_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            star_menu()
        elif choice == "2":
            planet_menu()
        elif choice == "3":
            species_menu()
        elif choice == "4":
            civilization_menu()
        else:
            print("BLACK HOLE OF NOTHINGNESS")


def top_menu():
    scan_print(
        """Please select an option:
_________________________________________________
0. Exit the astral plane
1. Browse Stars
2. Browse Planets
3. Browse Species
4. Browse Civilizations""",0.01
    )
    
def star_menu():
    while True:
        scan_print(
            """Please select an option:
    _________________________________________________
    0. Back to main menu
    1. List Stars
    2. Find Star by ID
    3. Find Star by Type
    4. Create Star
    5. Update Star
    6. Delete Star""",0.01
        )
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_stars()
        elif choice == "2":
            find_star_by_id()
        elif choice == "3":
            find_star_by_type()
        elif choice == "4":
            create_star()
        elif choice == "5":
            update_star()
        elif choice == "6":
            delete_star()
            
def planet_menu():
    while True:
        scan_print(
            """Please select an option:
    _________________________________________________
    0. Back to main menu
    1. List Planets
    2. Find Planet by ID
    3. Find Planet by Type
    4. Create Planet
    5. Update Planet
    6. Delete Planet""",0.01
        )
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_planets()
        elif choice == "2":
            find_planet_by_id()
        elif choice == "3":
            find_planet_by_type()
        elif choice == "4":
            create_planet()
        elif choice == "5":
            update_planet()
        elif choice == "6":
            delete_planet()
            
def species_menu():
    while True:
        scan_print(
            """Please select an option:
    _________________________________________________
    0. Back to main menu
    1. List Species
    2. Find Species by ID
    3. Find Species by Type
    4. Create Species
    5. Update Species
    6. Delete Species""",0.01
        )
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_species()
        elif choice == "2":
            find_species_by_id()
        elif choice == "3":
            find_species_by_type()
        elif choice == "4":
            create_species()
        elif choice == "5":
            update_species()
        elif choice == "6":
            delete_species()
            
def civilization_menu():
    while True:
        scan_print(
            """Please select an option:
    _________________________________________________
    0. Back to main menu
    1. List Civilizations
    2. Find Civilization by ID
    3. Find Civilization by Type
    4. Create Civilization
    5. Update Civilization
    6. Delete Civilization""",0.01
        )
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_civilizations()
        elif choice == "2":
            find_civilization_by_id()
        elif choice == "3":
            find_civilization_by_type()
        elif choice == "4":
            create_civilization()
        elif choice == "5":
            update_civilization()
        elif choice == "6":
            delete_civilization()
          


if __name__ == "__main__":
    main()
