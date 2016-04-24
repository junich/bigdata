import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import json

search_keyword = "blade"

url = "http://www.omdbapi.com/?s=%s&r=json"

response = urllib2.urlopen(url % (search_keyword))
data = json.load(response)

header = ['Title', 'Type', 'Year', 'imdbID']
body = [header]
for item in data['Search']:
    line = []
    line.append(item['Title'])
    line.append(item['Type'])
    line.append(item['Year'])
    line.append(item['imdbID'])
    body.append(line)

import csv
file_nm = '%s.csv' % (search_keyword)
f = open(file_nm, 'w')
csv.writer(f).writerows(body)
f.close()
