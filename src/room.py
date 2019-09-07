# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, descrip, items):
        # n_to, s_to, e_to, w_to
        self.name = name
        self.descrip = descrip
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __repr__(self):
        return f"name: {self.name}, description: {self.descrip}"
