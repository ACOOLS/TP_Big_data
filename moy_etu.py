#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.database_tp

    moy_etu = db.etudiants.find({'notes.0': {'$lt': 15}})

    for e_etu in moy_etu:
        print(e_etu['nom'])