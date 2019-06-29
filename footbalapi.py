import http.client
import json 
from configparser import ConfigParser
import csv


config = ConfigParser()

config.read('config.ini')
api = config.get('Api','api')
uri = config.get('Api','uri')
headers = config.get('Api','headers')
plan = config.get('Api','plan')
token = config.get('Api','token')
v2 = config.get('Api','v2')

connection = http.client.HTTPConnection(api)
headers = {'X=Auth_token':token}
connection.request('GET',v2+uri,None,headers)
response = json.loads(connection.getresponse().read().decode())
#print (response)
#outfile= open('leauge.csv','w')
type(response)


#for c in response['competitions']:
    #print (c['area']['id'], c['area']['name'])


