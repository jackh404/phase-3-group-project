#lib/models/body.py
from models.__init__ import CURSOR, CONN
from models.model import Model
class Body(Model):
    
    # # # # # # # # # # # # # # # # # # #
    #          Class Properties         #
    # # # # # # # # # # # # # # # # # # #
    all = {}
    table = None
    columns = '(name, type, description, diameter, mass)'
    create_columns = '(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT, diameter REAL, mass REAL)'
    
    # # # # # # # # # # # # # # # # # # #
    #          Class Methods            #
    # # # # # # # # # # # # # # # # # # #
    @classmethod
    def create(cls, name, type, description, diameter, mass):
        """Create an instance of the class and save it to the database"""
        body = cls(name, type, description, diameter, mass)
        body.save()
        return body
    @classmethod
    def instance_from_db(cls, row):
        """Create an instance from a row of the database"""
        [id,name,type,description,diameter,mass] = row
        body = cls.all.get(id)
        if body:
            body.name = name
            body.type = type
            body.description = description
            body.diameter = diameter
            body.mass = mass
        else:
            body = cls(name, type, description, diameter, mass)
            body.id = id
            cls.all[id] = body
        return body
    
    def __init__(self, name, type, description, diameter, mass, id=None):
        super().__init__(name, type, description, id)
        self.diameter = diameter
        self.mass = mass
        
    # # # # # # # # # # # # # # # # # # # #
    #          Instance Methods           #
    # # # # # # # # # # # # # # # # # # # #
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
        
    def update(self):
        """Update an instance of the class in the database"""
        sql = f"""
        UPDATE {self.table} 
        SET name = ?, type = ?, description = ?, diameter = ?, mass = ? 
        WHERE id = ?;
        """
        CURSOR.execute(sql,(self.name, self.type, self.description, self.diameter, self.mass, self.id))
        CONN.commit()
    
    # # # # # # # # # # # # # # # # # # # #
    #          Instance Properties        #
    # # # # # # # # # # # # # # # # # # # #    
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