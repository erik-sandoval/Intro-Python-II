
class Item():
    def __init__(self, name, descr):
        self.name = name
        self.descr = descr

    def __repr__(self):
        return f"item: {self.name}, description: {self.descr}"
