import http.client
import json
from urllib.parse import urlencode

class BaseHeaders:
    def getBase():
        pass

class Headers(BaseHeaders):
    def getBase(self = None):
        return {"Content-Type" : "application/json", "Accept" : "application/json"}

class Client:
    def connect(domain, port):
        pass
    def close():
        pass
    def getData():
        pass

class POSTClient(Client):
    def post(url, body, headers):
        pass
class GETClient(Client):
    def get(url, params, headers):
        pass
    def setHeader(key, value):
        pass

#AUTH IMPL
class AuthClient(POSTClient):
    def __init__(self, headers = Headers.getBase()):
        self.headers = headers
    def connect(self, domain, port = 443):
        self.conn = http.client.HTTPSConnection(domain, port)
    def post(self, url, body , headers = {}):
        if headers:
            self.headers = headers
        self.conn.request("POST", url, json.dumps(body), self.headers)
        response = self.conn.getresponse()
        data  = response.read()
        print(data)
        self.data = data.decode("utf-8")
    def getData(self):
        return self.data
    def close(self):
        self.conn.close()

class GenericGETClient(GETClient):
    def __init__(self, headers = Headers.getBase()):
        self.headers = headers
    def connect(self, domain, port = 443):
        self.conn = http.client.HTTPSConnection(domain, port)
    def get(self, url, body= {}, headers = {}):
        if headers:
            self.headers = headers
        if body:
            url += "?" +  urlencode(body)
        self.conn.request("GET", url, headers = self.headers)
        response = self.conn.getresponse()
        data = response.read()
        self.data = data.decode("utf-8")
    def setHeader(self, key, value):
        self.headers[key] = value
    def close(self):
        self.conn.close()
    def getData(self):
        pass

#JWT IMPL
class JwtClient(GenericGETClient):
    def getData(self):
        return self.data

class STRGETClient(GenericGETClient):
    def getData(self):
        return self.data

class JSONGETClient(GenericGETClient):
    def getData(self):
        return json.loads(self.data)





