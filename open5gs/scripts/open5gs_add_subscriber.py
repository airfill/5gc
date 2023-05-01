# SPDX-License-Identifier: GPL-3.0-or-later

'''
    Created and tested by airfill.io 
    Adds a subscribers to open5GS MongoDB database 
    Example Usage: python3 open5gs_add_subscriber.py --imsi IMSI --k K --opc OPc (--apn DNN/APN)
'''
import argparse
import pymongo
from bson.objectid import ObjectId


parser = argparse.ArgumentParser(description='Add subscriber to open5GS MongoDB HSS')
parser.add_argument('--imsi', required=True, help='IMSI value')
parser.add_argument('--k', required=True, help='K value')
parser.add_argument('--opc', required=True, help='OPc value')
parser.add_argument('--apn', default='internet', help='Session DNN/APN')
args = parser.parse_args()

session_data = {
    '_id': ObjectId(),
    'name': args.apn,
    'type': 3,
    'pcc_rule': [],
    'ambr': {'uplink': {'value': 1, 'unit': 3}, 'downlink': {'value': 1, 'unit': 3}},
    'qos': {'index': 9, 'arp': {'priority_level': 8, 'pre_emption_capability': 1, 'pre_emption_vulnerability': 1}}
}

slice_data = [
    {
        '_id': ObjectId(),
        'sst': 1,
        'default_indicator': True,
        'session': [session_data]
    }
]

subc_data = {
    'imsi': args.imsi,
    'subscribed_rau_tau_timer': 12,
    'network_access_mode': 0,
    'subscriber_status': 0,
    'access_restriction_data': 32,
    'slice': slice_data,
    'ambr': {'uplink': {'value': 1, 'unit': 3}, 'downlink': {'value': 1, 'unit': 3}},
    'security': {'k': args.k, 'amf': '8000', 'op': None, 'opc': args.opc},
    'schema_version': 1,
    '__v': 0
}

myclient = pymongo.MongoClient('mongodb://localhost')
mydb = myclient['open5gs']
mycol = mydb['subscribers']

# Check if the imsi already exists in the database
if mycol.find_one({"imsi": subc_data["imsi"]}) is not None:
    print(f"Subscriber with imsi {subc_data['imsi']} already exists in the database.")
else:
    # Insert the new document
    x = mycol.insert_one(subc_data)
    print("Added subscriber with Inserted ID : " + str(x.inserted_id))


