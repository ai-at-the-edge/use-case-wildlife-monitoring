import csv
import requests
import os

# iNaturalist export: (https://www.inaturalist.org/observations/export)

# Trap animal query:
# Query q=Callosciurus+finlaysonii&search_on=names&has%5B%5D=photos&quality_grade=any&identifications=any
# Columns id, user_login, quality_grade, license, url, image_url

# Other "unknown" Netherlands images query:
# Query search_on=place&has[]=photos&quality_grade=any&identifications=any&iconic_taxa[]=unknown&place_id=7506
# Columns id, user_login, quality_grade, license, url, image_url

# edge-impulse-uploader --api-key EI_API_KEY ./unknown/*

directory = "unknown" # Replace directory name, i.e. 'unknown' or 'animal'
if not os.path.exists(directory):
    os.makedirs(directory)
with open("observations-xxx.csv", 'r') as f: # Replace csv filename
   reader = csv.reader(f)
   next(reader, None) # skip header row
   for data in reader:
        # filename is constructed as id.user_login.extension
        filename = (directory + "/" + str(data[0]) + "." + str(data[1]) +
                    "." + str(data[5].rsplit('.', 1)[-1]))
        img = requests.get(data[5]).content
        with open(filename, 'wb') as handler:
            handler.write(img)
