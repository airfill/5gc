# SPDX-License-Identifier: GPL-3.0-or-later

'''
    Created and tested by airfill.io 
    Deletes a subscriber from open5GS MongoDB database 
    Example Usage: python3 open5gs_delete_subscriber.py --imsi IMSI
'''
import argparse
import pymongo

# connect to the database
myclient = pymongo.MongoClient("mongodb://localhost")
mydb = myclient["open5gs"]
mycol = mydb["subscribers"]

# parse the command-line arguments
parser = argparse.ArgumentParser(description="Delete a subscriber from the database.")
parser.add_argument("--imsi", help="IMSI of the subscriber to delete", required=True)
args = parser.parse_args()

# delete the subscriber with the given IMSI
result = mycol.delete_one({"imsi": args.imsi})
if result.deleted_count == 1:
    print(f"Subscriber with IMSI {args.imsi} deleted successfully.")
else:
    print(f"No subscriber found with IMSI {args.imsi}.")

