#!/usr/bin/env python3

from helpers import (
    exit_program,
    list_stars,
    find_star_by_type,
    find_star_by_id,
    create_star,
    update_star,
    delete_star,
    list_star_planets,
    list_planets,
    find_planet_by_type,
    find_planet_by_name,
    find_planet_by_id,
    find_planet_by_star_id,
    create_planet,
    update_planet,
    delete_planet,
    list_civilizations,
    find_civilization_by_type,
    find_civilization_by_name,
    find_civilization_by_id,
    find_civilization_by_species_id,
    find_civilization_by_planet_id, 
    find_civilization_by_star_id,
    create_civilization,
    update_civilization,
    delete_civilization,
    list_civilizations_species,
    list_species,
    find_species_by_type,
    find_species_by_id,
    find_species_by_civilization_id,
    find_species_by_planet_id,
    find_species_by_star_id,
    create_species,
    update_species,
    delete_species,
    initialize_from_database
)
    
    
    
    


def main():
    initialize_from_database()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_stars()
        elif choice == "2":
            find_star_by_type()
        elif choice == "3":
            find_star_by_id()
        elif choice == "4":
            create_star()
        elif choice == "5":
            update_star()
        elif choice == "6":
            delete_star()
        elif choice == "7":
            list_star_planets()
        elif choice == "8":
            list_planets()
        elif choice == "9":
            find_planet_by_type()
        elif choice == "10":
            find_planet_by_name()
        elif choice == "11":
            find_planet_by_id()
        elif choice == "12":
            find_planet_by_star_id()
        elif choice == "13":
            create_planet()
        elif choice == "14":
            update_planet()
        elif choice == "15":
            delete_planet()
        elif choice == "16":
            list_civilizations()
        elif choice == "17":
            find_civilization_by_type()
        elif choice == "18":
            find_civilization_by_name()
        elif choice == "19":
            find_civilization_by_id()
        elif choice == "20":
            find_civilization_by_species_id()
            
            
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
