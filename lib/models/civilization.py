from models.__init__ import CURSOR, CONN
from models.model import Model
class Civilization(Model):
    all = {}
    table = 'civilizations'
    columns = '(name, type, description)'
    create_columns = '(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT)'
    def __init__(self, name, type, description, id=None):
        super().__init__(name, type, description, id)
    @classmethod
    def create(cls, name, type, description):
        """Create an instance of the class and save it to the database"""
        thing = cls(name, type, description)
        thing.save()
        return thing
    def save(self):
        """Save current instance of the class to the database"""
        sql = f"""
        INSERT INTO {self.table} {self.columns}
        VALUES (?, ?, ?);
        """
        CURSOR.execute(sql,(self.name, self.type, self.description))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self