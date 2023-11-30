#!/usr/bin/env python3

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
    find_civilation_by_type,
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
)
    
    
    
    


def main():
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
            list_planets()
        elif choice == "8":
            find_planet_by_type()
        elif choice == "9":
            find_planet_by_id()
        elif choice == "10":
            create_planet()
        elif choice == "11":
            update_planet()
        elif choice == "12":
            delete_planet()
        elif choice == "13":
            list_civilizations()
        elif choice == "14":
            find_civilizations_by_type()
        elif choice == "15":
            find_civilization_by_id()
        elif choice == "16":
            create_civilization()
        elif choice == "17":
            update_civilization()
        elif choice == "18":
            delete_civilization()
        elif choice == "19":
            list_species()
        elif choice == "20":
            find_species_by_type()
        elif choice == "21":
            find_species_by_id()
        elif choice == "22":
            create_species()
        elif choice == "23":
            update_species()
        elif choice == "24":
            delete_species()
            
            
        else:
            print("BLACK HOLE OF NOTHINGNESS")


def menu():
    print("Please select an option:")
    print("0. Exit the astral plane")
    print("1. List all stars")
    print("2. Find star by type")
    print("3. Find star by id")
    print("4. Create new star")
    print("5. Update star")
    print("6. Delete star")
    print("7. List all planets")
    print("8. Find planet by type")
    print("9. Find planet by id")
    print("10. Create planet")
    print("11. Update planet")
    print("12. Delete planet")
    print("13. List civilizations")
    print("14. Find civilization by type")
    print("15. Find civilization by id")
    print("16. Create civilization")
    print("17. Update civilization")
    print("18. Delete civilization")
    print("19. List species")
    print("20. Find species by type")
    print("21. Find species by id")
    print("22. Create species")
    print("23. Update species")
    print("24. Delete species")
    
    
          


if __name__ == "__main__":
    main()
