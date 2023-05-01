# SPDX-License-Identifier: GPL-3.0-or-later

'''
    Created and tested by airfill.io 
    Lists all of the subscribers in open5GS MongoDB database 
    Example Usage: python3 open5gs_list_subscribers.py
'''
import json
import pymongo
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)

myclient = pymongo.MongoClient("mongodb://localhost")
mydb = myclient["open5gs"]
mycol = mydb["subscribers"]

i = 0
for doc in mycol.find():
    i += 1
    print(json.dumps(doc, cls=JSONEncoder, indent=4))
    
print(f'\n :: There are {i} subscribers in HSS :: \n')    

