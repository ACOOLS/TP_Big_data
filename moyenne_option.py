#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.database_tp

    agr = [ { '$group' :{'_id':'$option', 'moyenne':{'$avg' :{ '$arrayElemAt':['$notes',2]}}}}]

    val = list(db.etudiants.aggregate(agr))

    for valeur in val:
    	print('La moyenne des étudiants de l option', valeur['_id'], 'est de {}'.format( valeur['moyenne']))
   