# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, descrip):
        # n_to, s_to, e_to, w_to
        self.name = name
        self.descrip = descrip
        # self.n_to = n_to
        # self.s_to = s_to
        # self.e_to = e_to
        # self.w_to = w_to

    def __repr__(self):
        return f"name: {self.name}, description: {self.descrip}"
