#!/usr/bin/env python3
# lib/debug.py
from models.planet import Planet
from models.star import Star
from models.species import Species
from models.civilization import Civilization
from models.__init__ import CONN, CURSOR
class Seeder:
    def main():
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
        Star.create("Alpha Centauri", "star system", "A system of three stars: Rigil Kentaurus, Toliman, and Proxima Centauri",2.889e6,3.976e30)
        Star.create("Agillae", "orange dwarf", "One of the Scoured stars, it is orbited by five terrestrial planets",928456,589185185185185185)
        Star.create("Bastiar", "yellow dwarf", "One of the Scoured Stars, it is orbited by eight planets of various types.",1392684,1988500000000000000)
        Star.create("Callion", "red dwarf", "One of the Scoured Stars, it is orbited by two tidally locked planets which are always on opposite sides of the star.",696342,248562500000000000)
        Star.create("Ghavaniska", 'blue giant', "The Ghavaniska system consists of the blue star Ghavaniska, its eight planets, their moons, and the space station Conqueror's Forge, which moves across the system.",2.889e6,3.976e30)

        Planet.create("Earth", "terrestrial", "The only habitable planet in our solar system",12742,597200000000,1,1,1)
        Planet.create("Castrovel", "terrestrial", "Wild jungle planet, birthplace of the Lashunta",12742,597200000000,1,1,2)
        Planet.create("Abalon", "desolate waste", "Rocky planet with a very thin atmosphere, largely covered in machinery",12742,597200000000,.5,.5,2)
        Planet.create("Bastiar 1", "desolate waste", "A small scorched rock too close to Bastiar to be inhabitable.",1274,597200000,.5,.25,5)
        Planet.create("Bastiar 2", "terrestrial", "An earth-sized planet in the hottest orbit of Bastiar that could still be habitable",12740,597200000000,.75,.6,5)
        Planet.create("Bastiar 3", "terrestrial", "An earth-sized planet with a wildly eccentric orbit that results in extreme seasons over a very long year",12740,597200000000,1.5,45,5)
        Planet.create("Bastiar 4", "terrestrial", "Wild jungle planet with an eccentric orbit.",12742,597200000000,1.9,12,5)
        Planet.create("Mars", "desolate waste", "Known as the Red Planet, and named for the Roman god of war. Mars may have had water on it once.",6792,6.42e14,1,1.88,1)
        Planet.create("Mercury", "desolate waste", "Mercury is the first planet from the Sun and the smallest in the Solar System.",4880,3.3e14,176,0.24,1)
        Planet.create("Venus", "terrestrial", "Venus is the second planet from the Sun. It is a rocky planet with the densest atmosphere of all the rocky bodies in the Solar System, and the only one with a mass and size that is close to that of its orbital neighbour Earth.",12100,4.8685e14,243,0.61,1)
        Planet.create("Vesk Prime", "terrestrial", "Vesk Prime is a large, hot, dry, resource-rich terrestrial planet with a single moon named Yterakesh. It is the capital of the Vesk Imperium.",28669,2986000000000,1.15,3,7)
        Planet.create("Yterakesh", "terrestrial", "Yterakesh is a moon of Vesk Prime",2866,2986000000,.3,.1,7)

        Species.create("Human", "humanoid", "A featherless biped",1)
        Species.create("Canis familiaris", "mammal", "Domesticated dogs, commonly known as 'man's best friend'",1)
        Species.create("Lashunta", "humanoid", "Perfectly symmetrical beings with low-level telepathy. They are bimorphic.",2)
        Species.create("Android", "synthetic", "Synthetic beings, typically with a humanoid form",3)
        Species.create("Vesk", "reptilian", "Vesk average about 7 feet in height. They are warm-blooded and have an imposing appearance, possessing tough green scales, powerful muscles, long, thick tails, small horns, claws and teeth.",11)

        Civilization.create("European Union", "continental", "A group of countries on the continent of Europe", "Christianity, Judaism, Islam, Hinduism","English, Spanish, French, German, Austrian", [1], [1])
        Civilization.create("The Pact Worlds","system-wide","A group of worlds that banded together when their solar system was invaded by the Vesk","Sarenrae, Iomadae, Pharasma","Common, Castrovellian, Eoxian, Elvish", [2,3], [2,3])
        Civilization.create("The Veskarium","system-wide","An Empire of Vesk that conqured their solar system and are still looking to expand.","Damoritosh","Common, Vesk", [4], [11,12])
