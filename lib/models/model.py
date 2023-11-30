#lib/models/model.py
from models.__init__ import CURSOR, CONN
class Model:
    # # # # # # # # # # # # # # # # # # #
    #          Class Properties         #
    # # # # # # # # # # # # # # # # # # #
    #dictionary of all instances of the class
    all = {}
    #table name, to be overriden by child classes
    table = None
    #columns in the table
    columns = '(name, type, description)'
    #columns to be created with types for the table
    create_columns = '(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT)'
    #list of types of object, to be overriden by child classes
    types = []
    
    # # # # # # # # # # # # # # # # # # #
    #          Class Methods            #
    # # # # # # # # # # # # # # # # # # #
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
        model = cls(name, type, description)
        model.save()
        return model
    
    @classmethod
    def instance_from_db(cls, row):
        """Create an instance from a row of the database"""
        [id,name,type,description] = row
        model = cls.all.get(id)
        if model:
            model.name = name
            model.type = type
            model.description = description
        else:
            model = cls(name, type, description)
            model.id = id
            cls.all[id] = model
        return model
    
    @classmethod
    def get_all(cls):
        """Get all instances of the class from the database"""
        sql = f"""
        SELECT * FROM {cls.table};
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Get an instance of the class from the database"""
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        sql = f"""
        SELECT * FROM {cls.table} WHERE id = ?;
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Get an instance of the class from the database based on its name"""
        if not isinstance(name, str) or not len(name):
            raise TypeError("Name must be a non-empty string")
        sql = f"""
        SELECT * FROM {cls.table} WHERE name = ?;
        """
        row = CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_type(cls, type):
        """Get an instance of the class from the database based on its type"""
        if not isinstance(type, str) or not len(type):
            raise TypeError("Type must be a non-empty string")
        sql = f"""
        SELECT * FROM {cls.table} WHERE type = ?;
        """
        rows = CURSOR.execute(sql,(type,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def __init__(self, name, type, description, id=None):
        self.name = name
        self.type = type
        self.description = description
        self.id = id
        
    # # # # # # # # # # # # # # # # # # # #
    #          Instance Methods           #
    # # # # # # # # # # # # # # # # # # # #
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
        
    def update(self):
        """Update an instance of the class in the database"""
        sql = f"""
        UPDATE {self.table} 
        SET name = ?, type = ?, description = ? 
        WHERE id = ?;
        """
        CURSOR.execute(sql,(self.name, self.type, self.description, self.id))
        CONN.commit()
    
    def delete(self):
        """Delete current instance of the class from the database"""
        sql = f"""
        DELETE FROM {self.table} 
        WHERE id = ?;
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]
        # Set the id to None
        self.id = None
    
    #Return string representation of current object. Implicitly called by print(instance)
    def __str__(self):
        return f"{type(self).__name__} Name: {self.name}\nType: {self.type}\nDescription: {self.description}"
    
    # # # # # # # # # # # # # # # # # # # #
    #          Instance Properties        #
    # # # # # # # # # # # # # # # # # # # #   
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
    def type(self, value):
        if value not in type(self).types:
            raise ValueError(f"Type must be one of {type(self).types}")
        self._type = value

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        if not isinstance(value, str) or not len(value):
            raise TypeError("Description must be a non-empty string")
        self._description = value
