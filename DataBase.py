import pymongo

# UniteBot Cluster
cluster = pymongo.MongoClient("mongodb+srv://Vishan:harsha@unitebot.jmii40m.mongodb.net/?retryWrites=true&w=majority")

# UniteBot Database
database = cluster['UniteBot']

# Collections
communities = database["Communities"]
events = database["Events"]

distinctvalues = events.distinct("description")
