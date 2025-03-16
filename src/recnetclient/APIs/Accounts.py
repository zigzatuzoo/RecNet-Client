from ..fsclient import FlareSolverrClient

class Accounts:
    #https://apim.rec.net/accounts/account?username=Zigzatuzoo
    def GetAccountViaUsername(HTTPClient: FlareSolverrClient, Username: str):
        url = "https://apim.rec.net/accounts/account?username="+Username

        return HTTPClient.get(url)

    #Currently trying to fix sending auth through FlareSolverr
    def GetMe(HTTPClient : FlareSolverrClient):
        token = HTTPClient.get_token()
        url = "https://accounts.rec.net/account/me"

        headers = {"Authorization":token}

        return HTTPClient.get_headers(url,headers)