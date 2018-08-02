import requests


class Client_Class:
    def __init__(self):
        return
    @staticmethod

    def get_client():
        h = requests.get('http://pythonredjaguars-env.hx2tdpc8dz.us-east-2.elasticbeanstalk.com/')
        return h

