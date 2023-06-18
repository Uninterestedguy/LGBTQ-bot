import pymongo

# UniteBot Cluster
cluster = pymongo.MongoClient("mongodb+srv://Vishan:harsha@unitebot.jmii40m.mongodb.net/?retryWrites=true&w=majority")

# UniteBot Database
db = cluster['UniteBot']

# Collections i.e tables
communities = db["Communities"]
events = db["Events"]
genders= db["Genders"]

def gender_query(gender):
    qr=db.Genders.find({'Gender':gender.lower()},{"Description":1,"_id":0})
    data=[j for j in qr]
    print(data[0]["Description"])

def comm_query(Location,Community):
    qr=db.Communities.find({'City of Organization/Program':Location,'Name of Organization/Program':Community})

def comm_query(Location):
    qr=db.Communities.find({'City of Organization/Program':Location})

def comm_query(Community):
    qr=db.Communities.find({'Name of Organization/Program':Community})

def event_query(Location,Event):
    qr=db.Events.find({'description':Event,'location':Location})

def event_query(Location):
    qr=db.Events.find({'location':Location})

def event_query(Event):
    qr=db.Events.find({'description':Event})
