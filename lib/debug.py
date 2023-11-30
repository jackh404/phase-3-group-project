#!/usr/bin/env python3
# lib/debug.py
import sys
sys.path.append('models')
from models.planet import Planet
from models.star import Star
from models.species import Species
from models.__init__ import CONN, CURSOR
import ipdb

Planet.drop_table()
Star.drop_table()
Species.drop_table()
Planet.create_table()
Star.create_table()
Species.create_table()


Star.create("Sol", "yellow dwarf", "A G-type main sequence star lovingly called the Sun",1392684,1988500000000000000)
Planet.create("Earth", "terrestrial", "The only habitable planet in our solar system",12742,597200000000,1,1,1)
Species.create("Human", "humanoid", "A featherless biped",1)
#ipdb.set_trace()
