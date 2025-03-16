from ..fsclient import FlareSolverrClient

class Images:
    def GetComments(HTTPClient : FlareSolverrClient, ImageID):
        """Returns the JSON information of the comments on an image"""

        url = f"https://apim.rec.net/apis/api/images/v1/{str(ImageID)}/comments"

        return HTTPClient.get(url)

"https://apim.rec.net/apis/api/images/v1/720425932/comments"