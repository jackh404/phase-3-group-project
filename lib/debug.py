#!/usr/bin/env python3
# lib/debug.py
from models.planet import Planet
from models.star import Star
from models.species import Species
from models.civilization import Civilization
from models.__init__ import CONN, CURSOR
from seed_db import Seeder
from atlas import main
import ipdb

Seeder.main()
main()
#ipdb.set_trace()
