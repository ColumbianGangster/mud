class Room(Obj):
    def __init__(self, name):
        self.exits = {}
        self.name = name

    def __repr__(self):
	return 'Room: %s (id %s) - exits %s' % (self.name, self.oid, '|'.join(self.exits.keys()))