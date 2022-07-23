import pymongo
client = pymongo.MongoClient("mongodb+srv://rajreddy25:13Forjob@cluster0.ioapdej.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "raj reddy",
    "email": "rnrkota@gmail.com",
    "surname": "kota"

}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

