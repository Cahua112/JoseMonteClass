#Class libraries for the bluetooth application

import time#Class Library

from bluetooth.ble import BeaconService#<------3rd party module

service = BeaconService()#Creating an instance object of the class library

service.start_advertising("11111111-2222-3333-4444-555555555555"1,1,1,200)#advertise the UUID and different ports for spoofing devices

time.sleep(15)#wait to run every 15 seconds
service.stop_adertise()

print("Done")