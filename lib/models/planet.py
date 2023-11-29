from models.body import Body

class Planet(Body):
    all = {}
    table = 'planets'
    columns  = '(id, name, type, description, diameter, mass, day, year)'
    create_columns = '(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT, diameter REAL, mass REAL, day REAL, year REAL)'
    types = ['terrestrial', 'gas giant', 'ice planet', 'ocean planet', 'desolate waste', 'living', 'garden world', 'other (see description)']

    def __init__(self, name, type,description, diameter, mass, day, year, star_id, id=None):
        super.__init__(name, type, description, diameter, mass, id)
        self.day = day
        self.year = year
        self.star_id = star_id
        
    def __str__(self):
        return f'{super().__str__()}\nDay: {self.day} Earth days\nYear: {self.year} Earth years\nStar: {self.star}'

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
        if value is int and Star.find_by_id(value):
            self._star_id = value
        else:
            raise TypeError("Star ID must be a valid star ID")
        self._star_id = value