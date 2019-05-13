import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'a83f3b89929d4c37bdb4b482ecd1696c' }
connection.request('GET', '/v2/players/10000', None, headers )
response = json.loads(connection.getresponse().read().decode())

print (response)
