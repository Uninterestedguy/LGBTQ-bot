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

def comm_query(Location=location,Community=community):
    db.Communities.find({'City of Organization/Program':Location,'Name of Organization/Program':Community})

def comm_query(Location=location):
    db.Communities.find({'City of Organization/Program':Location})

def comm_query(Community=community):
    db.Communities.find({'Name of Organization/Program':Community})

def event_query(Location=location,Event=event):
    db.Events.find({'description':Event,'location':Location'})

def event_query(Location=location):
    db.Events.find({'location':Location'})

def event_query(Event=event):
    db.Events.find({'description':Event})
