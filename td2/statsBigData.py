import pymongo as mongo
import statistics

mongoConnexion = mongo.MongoClient("localhost", 27017)

coll = mongoConnexion.get_database('BigDataTD').get_collection('Patients').find()

mydict = {}
moyenne_dict = {}
mediane_dict = {}
tab_mediane = {}
counter = 0
for doc in coll:
    for index, value in doc.items():
        if type(value) is float and index != 'IPP':
            mydict.update({index: value})
            if index in mydict:
                if counter == 0:
                    moyenne_dict.update({index: value})
                    tab_mediane.setdefault(index, [])
                    tab_mediane[index].append(value)
                    mediane_dict.update({index: tab_mediane[index]})
                else:
                    moyenne_dict.update({index: value+moyenne_dict[index]})
                    tab_mediane[index].append(value)
                    mediane_dict.update({index: tab_mediane[index]})
    counter = 1

for i, v in moyenne_dict.items():
    print ("Moyenne "+i+" : ", v/coll.count(True))

for y, w in mediane_dict.items():
    print ("Mediane "+y+" : ", statistics.median(w))

