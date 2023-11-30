from models.__init__ import CURSOR, CONN
from models.model import Model
from models.planet import Planet
from models.species import Species
class Civilization(Model):
    
    # # # # # # # # # # # # # # # # # # #
    #          Class Properties         #
    # # # # # # # # # # # # # # # # # # #
    all = {}
    table = 'civilizations'
    columns = '(name, type, description, religions, languages)'
    create_columns = '(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT, religions TEXT, languages TEXT)'
    civ_species = '(civilization_id, species_id)'
    civ_planets = '(civilization_id, planet_id)'
    types = ['continental','planetary','interplanetary','system-wide','interstellar']
    
    # # # # # # # # # # # # # # # # # # #
    #          Class Methods            #
    # # # # # # # # # # # # # # # # # # #
    @classmethod
    def create_tables(cls):
        """create the table in the database corresponding to the class, then create the join tables for the class"""
        super().create_table()
        sql = """CREATE TABLE IF NOT EXISTS civilization_species
        (civilization_id INTEGER, species_id INTEGER, FOREIGN KEY(civilization_id) REFERENCES civilizations(id), FOREIGN KEY(species_id) REFERENCES species(id));"""
        CURSOR.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS civilization_planets
        (civilization_id INTEGER, planet_id INTEGER, FOREIGN KEY(civilization_id) REFERENCES civilizations(id), FOREIGN KEY(planet_id) REFERENCES planets(id));"""
        CURSOR.execute(sql)
    
    @classmethod
    def drop_tables(cls):
        """Drop the tables that persists objects of this class"""
        super().drop_table()
        sql = """DROP TABLE IF EXISTS civilizations_species;"""
        CURSOR.execute(sql)
        sql = """DROP TABLE IF EXISTS civilizations_planets;"""
        CURSOR.execute(sql)
        
    @classmethod
    def create(cls, name, type, description, religions, languages, species_ids=[], planet_ids=[]):
        """Create an instance of the class and save it to the database"""
        civilization = cls(name, type, description, religions, languages, species_ids, planet_ids)
        civilization.save()
        return civilization
    
    def __init__(self, name, type, description, religions, languages, species_ids, planet_ids, id=None):
        super().__init__(name, type, description, id)
        self.species_ids = species_ids
        self.planet_ids = planet_ids
        self.religions = religions
        self.languages = languages
        
    # # # # # # # # # # # # # # # # # # # #
    #          Instance Methods           #
    # # # # # # # # # # # # # # # # # # # #
    def save(self):
        """Save current instance of the class to the database"""
        sql = f"""
        INSERT INTO {self.table} {self.columns}
        VALUES (?, ?, ?, ?, ?);
        """
        CURSOR.execute(sql,(self.name, self.type, self.description, self.religions, self.languages))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        self.join_tables()
        
    def join_tables(self):
        """Save the current instance's join tables to the database"""
        sql = f"""
        INSERT INTO civilization_species {self.civ_species}
        VALUES (?, ?);
        """
        for species_id in self.species_ids:
            CURSOR.execute(sql, (self.id, species_id))
        sql = f"""
        INSERT INTO civilization_planets {self.civ_planets}
        VALUES (?, ?);
        """
        for planet_id in self.planet_ids:
            CURSOR.execute(sql, (self.id, planet_id))
        CONN.commit()
    
    @property
    def species(self):
        return self._species
    @species.setter
    def species(self, value):
        if not isinstance(value, list) or not all(isinstance(x, Species) for x in value):
            raise TypeError("Species must be a list of Species objects")
        self._species = value
    
    @property
    def planets(self):
        return self._planets
    @planets.setter
    def planets(self, value):
        if not isinstance(value, list) or not all(isinstance(x, Planet) for x in value):
            raise TypeError("Planets must be a list of Planet objects")
        self._planets = value
    
    @property
    def religions(self):
        return self._religions
    @religions.setter
    def religions(self, value):
        if not isinstance(value, str) or not len(value):
            raise TypeError("Religions must be a non-empty string")
        self._religions = value
        
    @property
    def languages(self):
        return self._languages
    @languages.setter
    def languages(self, value):
        if not isinstance(value, str) or not len(value):
            raise TypeError("Languages must be a non-empty string")
        self._languages = value