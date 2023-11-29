#!/usr/bin/env python3
# lib/debug.py
import sys
sys.path.append('models')
from models.body import Body
from models.model import Model
from models.planet import Planet
from models.star import Star
from models.__init__ import CONN, CURSOR
import ipdb

Planet.drop_table()
Star.drop_table()
Planet.create_table()
Star.create_table()


ipdb.set_trace()
