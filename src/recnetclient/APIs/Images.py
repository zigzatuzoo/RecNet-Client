from ..fsclient import FlareSolverrClient
from ..exceptions import *

class Images:
    def GetComments(HTTPClient : FlareSolverrClient, ImageID):
        """Returns the JSON information of the comments on an image.
        
        Does NOT Requires Auth

        Returns: Success(Bool),Response(str or json)"""

        url = f"https://apim.rec.net/apis/api/images/v1/{str(ImageID)}/comments"

        return HTTPClient.get(url)


    def GetCheers(HTTPClient : FlareSolverrClient, ImageID):
        """Returns a list of UserIDs that have cheered an image.
        
        Does NOT Requires Auth

        Returns: Success(Bool),Response(str or json)"""

        url = f'https://apim.rec.net/apis/api/images/v1/{str(ImageID)}/cheers'

        return HTTPClient.get(url)

    
    def SendComment(HTTPClient : FlareSolverrClient, ImageID, Comment:str):
        """Posts a comment on an image using the Session token in your .env
        Does Requires Auth

        returns Success(Bool),Response(json)"""

        url = "https://api.rec.net/api/images/v2/comments"

        postdata = {
            'Comment':Comment,
            'SavedImageId':ImageID
        }

        token = HTTPClient.get_token()

        headers = {"Authorization":token}

        return HTTPClient.post_headers(url,headers,postdata)
