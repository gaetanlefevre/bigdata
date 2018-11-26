import pprint

import pymongo as mongo

mongoConnexion = mongo.MongoClient("localhost", 27017)

coll = mongoConnexion.get_database('BigDataTD').get_collection('Patients').find()
coll2 = mongoConnexion.get_database('BigDataTD').get_collection('PatientsCopie')

valeur = 0

for doc in coll:
    #pprint.pprint(doc)
    #print(doc['age'])
    valeur += doc['age']
    #coll2.insert_one(doc)

print('Moyenne age :', valeur/coll.count(True))