#lib/models/body.py
from models.model import Model
class Body(Model):
    
    all = {}
    table = None
    columns = '(id, name, type, description, diameter, mass)'
    create_columns = '(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT, diameter REAL, mass REAL)'
    
    
    def __init__(self, name, type, description, diameter, mass, id=None):
        super.__init__(name, type, description, id)
        self.diameter = diameter
        self.mass = mass
        
    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("Diameter must be a positive number (in km) expressed only in numeric format, ie 100000 not 1e5")
        self._diameter = value
    @property
    def mass(self):
        return self._mass
    @mass.setter
    def mass(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("Mass must be a positive number (in kg) expressed only in numeric format, ie 100000 not 1e5")
        self._mass = value
    
    def __str__(self):
        return f'{super().__str__()}\nDiameter: {format(self.diameter,"{:.2f}e")} km\nMass: {format(self.mass,"{:.2f}e")} kg'