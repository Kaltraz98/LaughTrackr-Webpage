class Location:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_location_details(self):
        return str(self)

    def __repr__(self):
        str = f"Name: {self.name}, Desciption: {self.description}\n"
        return str