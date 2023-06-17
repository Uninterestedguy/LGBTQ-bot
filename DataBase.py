import pymongo

# UniteBot Cluster
cluster = pymongo.MongoClient("mongodb+srv://Vishan:harsha@unitebot.jmii40m.mongodb.net/?retryWrites=true&w=majority")

# UniteBot Database
database = cluster['UniteBot']

# Collections i.e tables
communities = database["Communities"]
events = database["Events"]
genders= database["Genders"]

distinctvalues = events.distinct("description")

def gender_query(gender):
    db.Genders.find({'Gender':gender})
