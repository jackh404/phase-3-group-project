from models.body import Body
from models.__init__ import CURSOR, CONN

class Planet(Body):
    # # # # # # # # # # # # # # # # # # #
    #          Class Properties         #
    # # # # # # # # # # # # # # # # # # #
    all = {}
    table = 'planets'
    columns  = '(name, type, description, diameter, mass, day, year, star_id)'
    create_columns = '(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT, diameter REAL, mass REAL, day REAL, year REAL, star_id INTEGER)'
    types = ['terrestrial', 'gas giant', 'ice planet', 'ocean planet', 'desolate waste', 'living', 'garden world', 'other (see description)']

    # # # # # # # # # # # # # # # # # # #
    #          Class Methods            #
    # # # # # # # # # # # # # # # # # # #
    
    @classmethod
    def create(cls, name, type, description, diameter, mass, day, year, star_id):
        """Create an instance of the class and save it to the database"""
        planet = cls(name, type, description, diameter, mass, day, year, star_id)
        planet.save()
        return planet
    
    @classmethod
    def instance_from_db(cls, row):
        """Create an instance from a row of the database"""
        [id,name,type,description,diameter,mass,day,year,star_id] = row
        planet = cls.all.get(id)
        if planet:
            planet.name = name
            planet.type = type
            planet.description = description
            planet.diameter = diameter
            planet.mass = mass
            planet.day = day
            planet.year = year
            planet.star_id = star_id
        else:
            planet = cls(name, type, description, diameter, mass, day, year, star_id)
            planet.id = id
            cls.all[id] = planet
        return planet
    
    def __init__(self, name, type,description, diameter, mass, day, year, star_id, id=None):
        super().__init__(name, type, description, diameter, mass, id)
        self.day = day
        self.year = year
        self.star_id = star_id
        
    # # # # # # # # # # # # # # # # # # # #
    #          Instance Methods           #
    # # # # # # # # # # # # # # # # # # # #

    
    def save(self):
        """Save current instance of the class to the database"""
        sql = f"""
        INSERT INTO {self.table} {self.columns}
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        CURSOR.execute(sql,(self.name, self.type, self.description, self.diameter, self.mass, self.day, self.year, self.star_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        """Update an instance of the class in the database"""
        sql = f"""
        UPDATE {self.table} 
        SET name = ?, type = ?, description = ?, diameter = ?, mass = ?, day = ?, year = ?, star_id = ? 
        WHERE id = ?;
        """
        CURSOR.execute(sql,(self.name, self.type, self.description, self.diameter, self.mass, self.day, self.year, self.star_id, self.id))
        CONN.commit()
        
    def __str__(self):
        from models.star import Star
        return f'{super().__str__()}\nDay: {self.day} Earth days\nYear: {self.year} Earth years\nStar: {Star.find_by_id(self.star_id).name}'
    
    def native_species(self):
        from models.species import Species
        sql = f"""
        SELECT * FROM {Species.table} WHERE home_world_id = ?;
        """
        CURSOR.execute(sql,(self.id,))
        rows = CURSOR.fetchall()
        return [Species.instance_from_db(row) for row in rows]
    
    def civilizations(self):
        from models.civilization import Civilization
        return_list = []
        for civ in Civilization.all.values():
            if self.id in civ.planet_ids and civ not in return_list:
                return_list.append(civ)
        if return_list:
            return return_list
        else:
            return None
        
    def all_species(self):
        from models.species import Species
        return_list = self.native_species()
        for civ in self.civilizations():
            for species in civ.species():
                if species not in return_list:
                    return_list.append(species)
        if return_list:
            return return_list
        else:
            return None
        
        
    
    # # # # # # # # # # # # # # # # # # # #
    #          Instance Properties        #
    # # # # # # # # # # # # # # # # # # # #

    @property
    def day(self):
        return self._day
    @day.setter
    def day(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("Day length, expressed in earth days, must be a positive number")
        self._day = value

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("Year length, expressed in earth years, must be a positive number")
        self._year = value
        
    @property
    def star_id(self):
        return self._star_id
    @star_id.setter
    def star_id(self, value):
        from models.star import Star
        if Star.find_by_id(value):
            self._star_id = value
        else:
            raise TypeError("Star ID must be a valid star ID")
        self._star_id = value