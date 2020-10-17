import json
import csv

with open("nyc.geojson") as f:
  data = json.load(f)

# print(type(data['features']))#[2]['properties']['neighborhood'])

x = data['features']

# #Loop to gather all neighborhoods to use in filtering data

regionname = []
for i in range(len(x)):
    regionname.append(x[i]['properties']['neighborhood'])
    #print(x[i]['properties']['neighborhood']) #USE THIS TO CONFIRM THE NEIGHBORHOODS IN GEOJSON FILES

#print(regionname)

with open('listfile.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % region for region in regionname)