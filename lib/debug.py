#!/usr/bin/env python3
# lib/debug.py
import sys
sys.path.append('models')
from models.body import Body
from models.model import Model
from models.__init__ import CONN, CURSOR
import ipdb


Model.all[0] = "I am model 0"
Body.all[0] = "I am body 0"
print(Model.all[0])
print(Body.all[0])

ipdb.set_trace()
