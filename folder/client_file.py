import requests
import json


class Client_Class:
    def __init__(self):
        return

    @staticmethod
    def get_client():
        j = requests.get('http://pythonredjaguars-env.hx2tdpc8dz.us-east-2.elasticbeanstalk.com/api/recipe/Roasted Asparagus')
        h = requests.get('http://pythonredjaguars-env.hx2tdpc8dz.us-east-2.elasticbeanstalk.com/api/recipe/Big Night Pizza')
        r = requests.get('http://pythonredjaguars-env.hx2tdpc8dz.us-east-2.elasticbeanstalk.com/api/recipe/Crock Pot Roast')
        h = json.loads(h.text)
        j = json.loads(j.text)
        r = json.loads(r.text)
        print(h)
        print(j)
        print(r)
        return h, j, r
