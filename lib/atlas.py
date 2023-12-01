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
    create_planet, #Jack will work from here down V
    # update_planet,
    # delete_planet,
    list_civilizations,
    # find_civilization_by_type,
    # find_civilization_by_id,
    create_civilization,
    update_civilization,
    # delete_civilization,
    list_species,
    # find_species_by_type,
    # find_species_by_id,
    create_species,
    # update_species,
    # delete_species,
    intro,
    scan_print
)
    
def main():
    intro()
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
            find_civilization_by_type()
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
    scan_print(
        """Please select an option:
_________________________________________________
0. Exit the astral plane
1. List all stars
2. Find star by type
3. Find star by id
4. Create new star
5. Update star
6. Delete star
7. List all planets
8. Find planet by type
9. Find planet by id
10. Create planet
11. Update planet
12. Delete planet
13. List civilizations
14. Find civilization by type
15. Find civilization by id
16. Create civilization
17. Update civilization
18. Delete civilization
19. List species
20. Find species by type
21. Find species by id
22. Create species
23. Update species
24. Delete species""",0.001
    )
    
    
          


if __name__ == "__main__":
    main()
