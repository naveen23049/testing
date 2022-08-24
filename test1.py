import pymongo

client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb>@cluster0.ub7axwp.mongodb.net/?retryWrites=true&w=majority")
db = client.test


col=db['test2']

d1 = {
     "name" : "Naveen",
    "mail" : "naveenmail2304",
    "surname" : "Thota"
}

col.insert_one(d1)
