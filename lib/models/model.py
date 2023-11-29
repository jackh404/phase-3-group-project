#lib/models/model.py
from models.__init__ import CURSOR, CONN
class Model:
    #dictionary of all instances of the class
    all = {}
    #table name, to be overriden by child classes
    table = None
    #columns in the table
    columns = '(id, name, type, description)'
    #columns to be created with types for the table
    create_columns = '(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT)'
    #list of types of object, to be overriden by child classes
    types = []
    
    @classmethod
    def create_table(cls):
        if cls.table:
            """Create a table in the database corresponding to the class"""
            sql = f"""CREATE TABLE IF NOT EXISTS {cls.table} {cls.create_columns};"""
            CURSOR.execute(sql)
            CONN.commit()
        else:
            raise Exception(f"Table not defined for this class ({cls.__name__})")
        
    @classmethod
    def drop_table(cls):
        """Drop the table that persists objects of this class"""
        if cls.table:
            sql = f"""
            DROP TABLE IF EXISTS {cls.table};
        """
            CURSOR.execute(sql)
            CONN.commit()
        else:
            raise Exception(f"Table not defined for this class ({cls.__name__})")
    
    @classmethod
    def create(cls, name, type, description):
        """Create an instance of the class and save it to the database"""
        thing = cls(name, type, description)
        thing.save()
        return thing
    
    @classmethod
    def instance_from_db(cls, row):
        """Create an instance from a row of the database"""
        name = row[1]
        type = row[2]
        description = row[3]

        thing = cls.all.get(row[0])
        if thing:
            thing.name = name
            thing.type = type
            thing.description = description
        else:
            thing = cls(name, type, description)
            thing.id = row[0]
            cls.all[row[0]] = thing
        return thing
    
    @classmethod
    def get_all(cls):
        """Get all instances of the class from the database"""
        sql = f"""
        SELECT * FROM {cls.table};
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Get an instance of the class from the database"""
        sql = f"""
        SELECT * FROM {cls.table} WHERE id = ?;
        """
        CURSOR.execute(sql,(id,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Get an instance of the class from the database based on its name"""
        if not isinstance(name, str) or not len(name):
            raise TypeError("Name must be a non-empty string")
        sql = f"""
        SELECT * FROM {cls.table} WHERE name = ?;
        """
        CURSOR.execute(sql,(name,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None
    
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
    
    def __init__(self, name, type, description, id=None):
        self.name = name
        self.type = type
        self.description = description
        self.id = id
    
    #Return string representation of current object. Implicitly called by print(instance)
    def __str__(self):
        return f"Name: {self.name}\nType: {self.type}\nDescription: {self.description}"
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not len(value):
            raise TypeError("Name must be a non-empty string")
        self._name = value

    @property
    def type(self):
        return self._type
    @type.setter
    def type(cls, self, value):
        if value not in cls.types:
            raise ValueError(f"Type must be one of {cls.types}")
        self._type = value

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value
