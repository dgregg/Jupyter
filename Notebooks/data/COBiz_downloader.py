# -*- coding: utf-8 -*-
"""
Colorado Businesses downloader python program
Created on Fri November 7 12:07:50 2021

@author: Dawn Gregg
"""
import json
import requests
import datetime

# Initial settings that control the data download
cobizURL =  "https://data.colorado.gov/resource/4ykn-tg5h.json"
paramD = dict()
paramD["principalzipcode"] = 80211                            
paramD["$order"] = "entityformdate DESC"
paramD["$limit"] = 5

# open the URL using the request library
document = requests.get(cobizURL, paramD)
print(document.request.url)

# get the JSON text from the URL into a dictionary using the request library       
if document.status_code == 200 :
     js = document.json()
else:
     print("Error code=",document.status_code, document.request.url)
     js = json.loads("{}")

# Output first Record
print("\nFirst Business Reading")
print(js[0])

# Write JSON data to a file
fdumps = open('bizdata_json.txt', "w")
fdumps.write(json.dumps(js).strip())

# Make sure you close the file otherwise data may not be saved!
fdumps.close()

#Process JSON Data
biz_list = []

# Loop through JSON data (now a Python list  of dictionaries)
# Extract relevant data items and create CoBiz object
print("\nAll Businesses")
for biz in js:

    # get date and convert it to datetime object
    isodate = biz["entityformdate"]
    dt = datetime.datetime.fromisoformat(isodate)

    # Get rest of data from first entity    
    entity  = biz["entityname"]
    eid     = biz["entityid"]
    address = biz["principaladdress1"]
    city    = biz["principalcity"]
    zip     = biz["principalzipcode"]
    status  = biz["entitystatus"]

    # create new CoBizo object and append to biz_list
    biz_list.append((eid, entity, address, city, zip, dt, status))
    print(biz_list[-1])  # Print last biz added to biz_list