import json
import requests

class Api:
    credential = {
        "id" : "",
        "password":""
    }
    cookie = None
    
    API = {}
    endpoint = "https://judgeapi.u-aizu.ac.jp"
    path = {
        "session":"/session",
        "submit":"/submission"
    }
    
    post_header_base = {'content-type': 'application/json'}
    
    def __init__(self, user_id, password):
        for k, v in self.path.items():
            self.API[k] =  self.endpoint + v
        self.credential["id"] = user_id
        self.credential["password"] = password
        
        self._get_session()
    
    def _get_session(self):
        cred = {
            "id" : self.credential["id"],
            "password" : self.credential["password"]
        }
        
        resp = requests.post(
            self.API["session"],
            headers =  self.post_header_base,
            data = json.dumps(cred)
        )
        
        if resp.status_code != 200:
            raise AojApiError("authentication error", detail=resp)
        
        cookie = resp.cookies
        
    def submit(self, problem_id, lang, source_code):
        pass
        

class AojApiError(Exception):
    err_message = None
    err_detail = None
    
    def __init__(self, message, detail=None):
        self.set_message(message)
    
    def set_message(self, message, detail=None):
        self.err_message = message
        
    def get_message(self):
        return self.err_message
    
    def get_detail(self):
        return self.err_detail
    

