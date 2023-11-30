#lib/models/body.py
from models.__init__ import CURSOR, CONN
from models.model import Model
class Body(Model):
    
    all = {}
    table = None
    columns = '(name, type, description, diameter, mass)'
    create_columns = '(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT, diameter REAL, mass REAL)'
    
    @classmethod
    def create(cls, name, type, description, diameter, mass):
        """Create an instance of the class and save it to the database"""
        thing = cls(name, type, description, diameter, mass)
        thing.save()
        return thing
    
    def __init__(self, name, type, description, diameter, mass, id=None):
        super().__init__(name, type, description, id)
        self.diameter = diameter
        self.mass = mass
        
    def save(self):
        """Save current instance of the class to the database"""
        sql = f"""
        INSERT INTO {self.table} {self.columns}
        VALUES (?, ?, ?, ?, ?);
        """
        CURSOR.execute(sql,(self.name, self.type, self.description, self.diameter, self.mass))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
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
            raise TypeError("Mass must be a positive number (in trillions of kg) expressed only in numeric format, ie 100000 not 1e5")
        self._mass = value
    
    def __str__(self):
        return f'{super().__str__()}\nDiameter: {format(self.diameter,"e")} km\nMass: {format(self.mass,"e")} trillion kg'