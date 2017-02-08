from urllib2 import urlopen
from json import load

#just a hypotetical case because the API key is missing
#coding lesson from codecademy.com

url = "http://api.npr.org/query?apiKey="
key = "API_KEY"
url = url + key
url += "&numResults=3&format=json"
url += "&id="
npr_id = raw_input("Which NPR ID do you want to query?")
url = url + npr_id
print url

response = urlopen(url)
json_obj = load(response)

for story in json_obj["list"]["story"]:
    print story["title"]["$text"]