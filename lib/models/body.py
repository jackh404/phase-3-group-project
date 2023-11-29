#lib/models/body.py
from models.__init__ import CURSOR, CONN
from models.model import Model
class Body(Model):
    
    all = {}
    table = None
    columns = '(name, type, description, diameter, mass)'
    create_columns = '(name TEXT, type TEXT, description TEXT, diameter REAL, mass REAL)'
    
    def __init__(self, name, type, description, diameter, mass, id=None):
        self.name = name
        self.type = type
        self.description = description
        self.diameter = diameter
        self.mass = mass
        self.id = id
        
    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
    @property
    def mass(self):
        return self._mass
    @mass.setter
    def mass(self, value):
        self._mass = value
    
    def __str__(self):
        return f'{super().__str__()}\nDiameter: {self.diameter}\nMass: {self.mass}'