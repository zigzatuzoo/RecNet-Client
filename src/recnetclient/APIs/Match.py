from ..fsclient import FlareSolverrClient
from ..exceptions import *

class Match:
    def GetMatchPlayer(HTTPClient: FlareSolverrClient, UserID):
        """Gets the match API data of a user.
        
        Does Require Session Token

        returns Success(Bool),Response(json)"""
        
        token = HTTPClient.get_token()

        headers = {
            'Authorization':token
        }

        url = "https://match.rec.net/player?id="+str(UserID)

        return HTTPClient.get_headers(url,headers)
    
