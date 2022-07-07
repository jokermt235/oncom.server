#Service factory register
from .clients import *
from django.conf import settings

class ServiceFactory:
    def __init__(self):
        self.__services = {}

    def register(self, name, service_class):
        # Maybe add some validation
        self.__services[name] = service_class

    def create(self, name, *args, **kwargs):
        # Maybe add some error handling or fallbacks
        return self.__services[name](*args, **kwargs)

factory = ServiceFactory()


class BaseService:
    def get(params):
        pass

class JwtService(BaseService):
    def get(self, params = {}):
        auth = AuthClient()
        auth.connect(settings.ON_AUTH_SERVER)
        auth.post("/api/login", {"username" : settings.ON_USERNAME , "password" : settings.ON_PASSWORD})
        token = auth.getData()
        auth.close()
        #JWT needed for oncom.be niether auth.mehub
        jwt  = JwtClient()
        jwt.connect(settings.ON_AUTH_SERVER)
        jwt.setHeader("Authorization", "Bearer " + token)
        jwt.get("/api/jwt", {"hostUid" : settings.ON_HOSTUID})
        jwt.close()
        return jwt.getData()

class GenericService(BaseService):
    def __init__(self):
        self.general = STRGETClient()
        self.general.connect(settings.ON_BE_SERVER)
        jwtService = JwtService()
        self.general.setHeader("Authorization", "Bearer " + jwtService.get())

    def get(self, params = {}):
        pass

class UidService(GenericService):
    def get(self, params  = {}):
        self.general.get("/api/profile/get-uid-by-iin", params)
        self.general.close()
        return self.general.getData()


class GeneralService(GenericService):
    def get(self, params = {}):
        uidService = UidService()
        params = {
            "uid" :  uidService.get(params)
        }
        self.general.get("/api/profile/get-general", params)
        self.general.close()
        return self.general.getData()

class CommonService(GenericService):
    def get(self, params = {}):
        uidService = UidService()
        params = {
            "uid" :  uidService.get(params)
        }
        self.general.get("/api/profile/get-common", params)
        self.general.close()
        return self.general.getData()



