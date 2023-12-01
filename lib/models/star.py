from models.body import Body
from models.__init__ import CURSOR, CONN

class Star(Body):
    table = 'stars'
    types = ['blue giant','star system','orange dwarf','red dwarf', 'red giant', 'white dwarf', 'main sequence', 'black hole', 'neutron star', 'brown dwarf','supergiant','yellow dwarf','proto','neutron','pulsar', 'other (see description)']
    
    def planets(self):
        from models.planet import Planet
        sql = f"""
        SELECT * FROM {Planet.table} WHERE star_id = ?;
        """
        CURSOR.execute(sql,(self.id,))
        rows = CURSOR.fetchall()
        return [Planet.instance_from_db(row) for row in rows]