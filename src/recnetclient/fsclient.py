#The FlareSolver Client

import httpx
from json import loads
import base64
from .exceptions import *
from .recnetlogin import RecNetLogin

import os
from dotenv import dotenv_values

class FlareSolverrClient:
    def __init__(self,
                 DotENV : str | None = None,
                 FSURL  : str = "https://flaresolverr.apps.zigzatuzoo.xyz/v1",
                 FSMURL : str = "localhost:8192",
                 SSLVer : bool = False):
        
        self.DotENV = DotENV
        self.client : httpx.Client = httpx.Client(verify=SSLVer)

        if DotENV == None:
            self.FlareSolverrURL = FSURL
            self.FSProxyURL = FSMURL
        else:
            env = dotenv_values(DotENV if DotENV else ".env.secret")
                
            key = 'FLARESOLVERR_INSTANCE'
            if key in env:
                self.FlareSolverrURL = env[key]
            else:
                if key in os.environ:
                    self.FlareSolverrURL = os.getenv(key)
                else:
                    raise InvalidFlareSolverrInstance

            key = 'FLARESOLVERR_MITMP_INSTANCE'
            if key in env:
                self.FSProxyURL = env[key]
            else:
                if key in os.environ:
                    self.FSProxyURL = os.getenv(key)
                else:
                    raise InvalidFlareSolverrMITMProxyInstance
                
        self.RNL = None

    def get_token(self):
        if not self.RNL:
            self.RNL = RecNetLogin(self.DotENV)
        
        return self.RNL.get_token(True)

    def get(self, url):
        """Sends a GET request through the FlareSolverr instance to the designated URL without any headers
        
        Returns: Success(Bool),Response(str or json)"""
        headers = {"Content-Type": "application/json"}
        data = {
            "cmd": "request.get",
            "url": url,
            "maxTimeout": 10000
        }

        resp = self.client.post(self.FlareSolverrURL,headers=headers,json=data)
        if resp.status_code == 200:
            data = resp.json()
        
            if data['solution']['status'] != 200:
                return False, "Request Error: "

            data = data['solution']['response']
            start = data.find('{')
            end = data.rfind('}')
            startb = data.find('[')
            endb = data.rfind(']')
            start = start if startb > start or startb == -1 else startb
            end = endb if start == startb else end

            info = data[start:end+1]
            data = loads(info)
            return True, data
        
        else:
            print(resp.text)
            return False, "FS Error: "+str(resp.status_code)
    
    def get_headers(self, url, headers : dict):
        """Sends a GET request through the FlareSolverr instance to the designated URL with specified headers
        
        Returns: Success(bool),Response(str or json)"""

        head = {"Content-Type": "application/json"}

        headerstr = "?" if (len(headers.keys()) > 0) and (not "?" in url) else ""
        for key in headers.keys():
            #$$headers[]=Authorization:mytoken
            headerstr += f'$$headers[]={key}:{headers[key]}'
            if key != list(headers.keys())[-1]: headerstr += "&"
        

        data = {
            "cmd": "request.get",
            "url": url+headerstr,
            "maxTimeout": 5000,
            "proxy": {
                "url": self.FSProxyURL
            }
        }

        resp = self.client.post(self.FlareSolverrURL,headers=head,json=data)
        if resp.status_code == 200:
            data = resp.json()
        
            data = data['solution']['response']
            start = data.find('{')
            end = data.rfind('}')
            startb = data.find('[')
            endb = data.rfind(']')
            start = start if startb > start or startb == -1 else startb
            end = endb if start == startb else end
            

            info = data[start:end+1]
            data = loads(info)
            return True, data
        
        else:
            print(resp.text)
            return False, "FS Error: "+str(resp.status_code)
    

    def post(self, url, postdata : dict):
        """Sends a POST request through the FlareSolverr instance to the designated URL without headers
        
        Returns: Success(bool),Response(str or json)"""

        pdata = base64.b64encode(str(postdata).replace("'",'"').encode('ascii'))

        headers = {"Content-Type": "application/json"}
        data = {
            "cmd": "request.get",
            "url": url,
            "maxTimeout": 5000,
            "proxy": {
                "url": self.FSProxyURL
            },
            "postData": "$$post="+pdata
        }

        resp = self.client.post(self.FlareSolverrURL,headers=headers,json=data)
        if resp.status_code == 200:
            data = resp.json()
        
            data = data['solution']['response']
            start = data.find('{')
            end = data.rfind('}')
            startb = data.find('[')
            endb = data.rfind(']')
            start = start if startb > start or startb == -1 else startb
            end = endb if start == startb else end

            info = data[start:end+1]
            data = loads(info)
            return True, data
        
        else:
            return False, "FS Error: "+str(resp.status_code)


    def post_headers(self, url, headers : dict, postdata : dict):
        """Sends a POST request through the FlareSolverr instance to the designated URL without headers
        
        Returns: Success(bool),Response(str or json)"""

        head = {"Content-Type": "application/json"}

        headerstr = "?" if (len(headers.keys()) > 0) and (not "?" in url) else ""
        for key in headers.keys():
            #$$headers[]=Authorization:mytoken
            headerstr += f'$$headers[]={key}:{headers[key]}'
            if key != list(headers.keys())[-1]: headerstr += "&"
        
        pdata = base64.b64encode(str(postdata).replace("'",'"').encode('ascii')).decode('ascii')

        data = {
            "cmd": "request.post",
            "url": url+headerstr,
            "maxTimeout": 5000,
            "proxy": {
                "url": self.FSProxyURL
            },
            "postData": "$$post="+pdata
        }

        resp = self.client.post(self.FlareSolverrURL,headers=head,json=data)
        if resp.status_code == 200:
            data = resp.json()

            data = data['solution']['response']
            start = data.find('{')
            end = data.rfind('}')
            startb = data.find('[')
            endb = data.rfind(']')
            start = start if startb > start or startb == -1 else startb
            end = endb if start == startb else end

            info = data[start:end+1]
            data = loads(info)
            return True, data
        
        else:
            return False, "FS Error: "+str(resp.status_code)