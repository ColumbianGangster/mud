import game_config
import filereading_config

class World(object):
    def __init__(self):
	try:
	    open(game_config.build_world(), filereading_config.read_only)
	except IOError:
	    print 'Building minimal world database ...',
	    f = open('db/world.yaml', 'w')
	    f.write(MINIMAL_DB)
	    f.close()
	    print 'Done.'
	print 'Loading world ...',
	self.db =  yaml.load(open('db/world.yaml', 'r'))
	if not isinstance(self.db, list): self.db = [ self.db ]
	self.dbtop = max([ x.oid for x in self.db ])
	print 'Done.'

	def save(self):
		f = open('db/world.yaml', 'w')
		f.write(yaml.dump(self.db))
		f.close()
	