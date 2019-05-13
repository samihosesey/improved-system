import requests
import json 
from configparser import ConfigParser


config = ConfigParser()

config.read('config.ini')
api = config.get('Api','api')
uri = config.get('Api','uri')
headers = config.get('Api','headers')
plan = config.get('Api','plan')

response = requests.get(api+"players/44")
if response.status_code == 200:
    print("200")
else :
    print("no")
