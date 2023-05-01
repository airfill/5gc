### open5gs Python scripts for MongoDB HSS

Add, delete and list subscribers
Tested with open5gs v2.6.2

Examples:

$ python3 open5gs_add_subscriber.py  `--`imsi 001010999900009 `--`k 0001ffff0001ffff08091111ffff0001 `--`opc 1111ffff2222ffff1111ffff888883ca `--`apn internet2

$ python3 open5gs_list_subscribers.py

$ python3 open5gs_delete_subscriber.py  `--`imsi 001010999900009