from ..fsclient import FlareSolverrClient
from ..exceptions import *

class Accounts:
    def GetAccountViaUsername(HTTPClient: FlareSolverrClient, Username: str):
        """Returns the userdata of a user using the Username provided.
        
        Does NOT Requires Auth

        Returns: Success(Bool),Response(str or json)"""
        url = "https://apim.rec.net/accounts/account?username="+Username

        return HTTPClient.get(url)


    #Currently trying to fix sending auth through FlareSolverr
    def GetMe(HTTPClient : FlareSolverrClient):
        raise AuthNotImplimentedYet
    
        token = HTTPClient.get_token()
        url = "https://accounts.rec.net/account/me"

        headers = {"Authorization":token}

        return HTTPClient.get_headers(url,headers)