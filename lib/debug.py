#!/usr/bin/env python3
# lib/debug.py
from models.planet import Planet
from models.star import Star
from models.species import Species
from models.civilization import Civilization
from models.__init__ import CONN, CURSOR
from atlas import main
import ipdb

Planet.drop_table()
Star.drop_table()
Species.drop_table()
Civilization.drop_tables()
Planet.create_table()
Star.create_table()
Species.create_table()
Civilization.create_tables()


Star.create("Sol", "yellow dwarf", "A G-type main sequence star lovingly called the Sun",1392684,1988500000000000000)
Star.create("Sarenrae", "yellow dwarf", "A G-type main sequence star that contains its own civilization known as 'The Burning Archipelago'",1392684,1988500000000000000)

Planet.create("Earth", "terrestrial", "The only habitable planet in our solar system",12742,597200000000,1,1,1)
Planet.create("Castrovel", "terrestrial", "Wild jungle planet, birthplace of the Lashunta",12742,597200000000,1,1,2)
Planet.create("Abalon", "desolate waste", "Rocky planet with a very thin atmosphere, largely covered in machinery",12742,597200000000,.5,.5,2)

Species.create("Human", "humanoid", "A featherless biped",1)
Species.create("Lashunta", "humanoid", "Perfectly symmetrical beings with low-level telepathy. They are bimorphic.",2)
Species.create("Android", "synthetic", "Synthetic beings, typically with a humanoid form",3)

Civilization.create("European Union", "continental", "A group of countries on the continent of Europe", "Christianity, Judaism, Islam, Hinduism","English, Spanish, French, German, Austrian", [1], [1])
Civilization.create("The Pact Worlds","system-wide","A group of worlds that banded together when their solar system was invaded by the Vesk","Sarenrae, Iomadae, Pharasma","Common, Castrovellian, Eoxian, Elvish", [2,3], [2,3])

main()
ipdb.set_trace()
