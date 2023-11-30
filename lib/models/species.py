from models.model import Model
from models.__init__ import CONN, CURSOR

class Species(Model):
    # # # # # # # # # # # # # # # # # # #
    #          Class Properties         #
    # # # # # # # # # # # # # # # # # # #
    all = {}
    table = 'species'
    columns = '(name, type, description, home_world_id)'
    create_columns = '(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT, home_world_id INTEGER)'
    types = ['humanoid', 'alien', 'insectoid', 'cephalapodic', 'amphibian', 'mammal', 'fish', 'reptilian', 'synthetic', 'undead', 'extraplanar']
    
    # # # # # # # # # # # # # # # # # # #
    #          Class Methods            #
    # # # # # # # # # # # # # # # # # # #
    
    @classmethod
    def create(cls, name, type, description, home_world_id):
        """Create an instance of the class and save it to the database"""
        species = cls(name, type, description, home_world_id)
        species.save()
        return species
    
    def __init__(self, name, type, description, home_world_id, id=None):
        super().__init__(name, type, description, id)
        self.home_world_id = home_world_id
        
    # # # # # # # # # # # # # # # # # # # #
    #          Instance Methods           #
    # # # # # # # # # # # # # # # # # # # #
    
        
    def save(self):
        """Save current instance of the class to the database"""
        sql = f"""
        INSERT INTO {self.table} {self.columns}
        VALUES (?, ?, ?, ?);
        """
        CURSOR.execute(sql,(self.name, self.type, self.description, self.home_world_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def __str__(self):
        return f"{super().__str__()}\nHome World id: {self.home_world_id}"
    
    @property
    def home_world_id(self):
        return self._home_world_id
    @home_world_id.setter
    def home_world_id(self, value):
        from models.planet import Planet
        if Planet.find_by_id(value):
            self._home_world_id = value
        else:
            raise TypeError("Home World ID must be a valid planet ID")
    