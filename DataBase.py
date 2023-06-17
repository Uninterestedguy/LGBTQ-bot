import pymongo

# UniteBot Cluster
cluster = pymongo.MongoClient("mongodb+srv://Vishan:harsha@unitebot.jmii40m.mongodb.net/?retryWrites=true&w=majority")

# UniteBot Database
db = cluster['UniteBot']

# Collections i.e tables
communities = db["Communities"]
events = db["Events"]
genders= db["Genders"]

distinctvalues = events.distinct("description")

def gender_query(gender):
    db.Genders.find({'Gender':gender})

def comm_query(Location,Community):
    db.Communities.find({'City of Organization/Program':Location,'Name of Organization/Program':Community})

def comm_query(Location):
    db.Communities.find({'City of Organization/Program':Location})

def comm_query(Community):
    db.Communities.find({'Name of Organization/Program':Community})

def event_query(Location,Event):
    db.Events.find({'description':Event,'location':Location})

def event_query(Location):
    db.Events.find({'location':Location})

def event_query(Event):
    db.Events.find({'description':Event})