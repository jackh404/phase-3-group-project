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
        sql = """CREATE TABLE IF NOT EXISTS civilizations_species
        (civilization_id INTEGER, species_id INTEGER, FOREIGN KEY(civilization_id) REFERENCES civilizations(id), FOREIGN KEY(species_id) REFERENCES species(id));"""
        CURSOR.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS civilizations_planets
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
        CONN.commit()
        
    @classmethod
    def create(cls, name, type, description, religions, languages, species_ids=[], planet_ids=[]):
        """Create an instance of the class and save it to the database"""
        civilization = cls(name, type, description, religions, languages, species_ids, planet_ids)
        civilization.save()
        return civilization
    
    @classmethod
    def instance_from_db(cls, row):
        """Create an instance from a row of the database"""
        [id,name,type,description,religions,languages] = row
        species_ids,planet_ids = cls.get_joins_from_db(id)
        civilization = cls.all.get(id)
        if civilization:
            civilization.name = name
            civilization.type = type
            civilization.description = description
            civilization.religions = religions
            civilization.languages = languages
            civilization.species_ids = species_ids
            civilization.planet_ids = planet_ids
        else:
            civilization = cls(name, type, description, religions, languages, species_ids, planet_ids)
            civilization.id = id
            cls.all[id] = civilization
        return civilization
    
    @classmethod
    def get_joins_from_db(cls, civ_id):
        """Get the join tables from the database"""
        sql = f"""
        SELECT species_id FROM civilizations_species WHERE civilization_id = ?;
        """
        CURSOR.execute(sql, (civ_id,))
        species_ids = [row[0] for row in CURSOR.fetchall()]
        
        sql = f"""
        SELECT planet_id FROM civilizations_planets WHERE civilization_id = ?;
        """
        CURSOR.execute(sql, (civ_id,))
        planet_ids = [row[0] for row in CURSOR.fetchall()]
        return species_ids, planet_ids
    
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
        """Delete potentially lingering joins and save the current instance's join tables to the database"""
        sql = f"""
        DELETE FROM civilizations_species WHERE civilization_id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        sql = f"""
        DELETE FROM civilizations_planets WHERE civilization_id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        sql = f"""
        INSERT INTO civilizations_species {self.civ_species}
        VALUES (?, ?);
        """
        for species_id in self.species_ids:
            CURSOR.execute(sql, (self.id, species_id))
        sql = f"""
        INSERT INTO civilizations_planets {self.civ_planets}
        VALUES (?, ?);
        """
        for planet_id in self.planet_ids:
            CURSOR.execute(sql, (self.id, planet_id))
        CONN.commit()
        
    def update(self):
        """Update an instance of the class in the database"""
        sql = f"""
        UPDATE {self.table} 
        SET name = ?, type = ?, description = ?, religions = ?, languages = ?
        WHERE id = ?;
        """
        CURSOR.execute(sql,(self.name, self.type, self.description, self.religions, self.languages, self.id))
        CONN.commit()
        self.join_tables()
        
    def planets(self):
        return [Planet.find_by_id(x) for x in self.planet_ids]
    
    def species(self):
        return [Species.find_by_id(x) for x in self.species_ids]
    
    def __str__(self):
        return f'{super().__str__()}\nReligions: {self.religions}\nLanguages: {self.languages}\nSpecies: {", ".join([Species.find_by_id(x).name for x in self.species_ids])}\nPlanets: {", ".join([Planet.find_by_id(x).name for x in self.planet_ids])}'
    
    # # # # # # # # # # # # # # # # # # # #
    #          Instance Properties        #
    # # # # # # # # # # # # # # # # # # # #
    
    @property
    def species_ids(self):
        return self._species_ids
    @species_ids.setter
    def species_ids(self, value):
        if all([num in Species.all.keys() for num in value]):
            self._species_ids = value
        else:
            raise ValueError("Species_ids must be a list of valid species ids")
        
    
    @property
    def planet_ids(self):
        return self._planet_ids
    @planet_ids.setter
    def planet_ids(self, value):
        if all([num in Planet.all.keys() for num in value]):
            self._planet_ids = value
        else:
            raise ValueError("Planet_ids must be a list of valid planet ids")
        
    @property
    def languages(self):
        return self._languages
    @languages.setter
    def languages(self, value):
        if isinstance(value, str) and len(value):
            self._languages = value
        else:
            raise ValueError("Languages must be a non-empty string")