from ..fsclient import FlareSolverrClient
from ..exceptions import *

class Images:
    def GetComments(HTTPClient : FlareSolverrClient, ImageID):
        """Returns the JSON information of the comments on an image.
        
        Returns: Success(Bool),Response(str or json)"""

        url = f"https://apim.rec.net/apis/api/images/v1/{str(ImageID)}/comments"

        return HTTPClient.get(url)


    def GetCheers(HTTPClient : FlareSolverrClient, ImageID):
        """Returns a list of UserIDs that have cheered an image.
        
        Returns: Success(Bool),Response(str or json)"""

        url = f'https://apim.rec.net/apis/api/images/v1/{str(ImageID)}/cheers'

        return HTTPClient.get(url)