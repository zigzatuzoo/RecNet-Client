from src import recnetclient as rnc
from src.recnetclient import RecNetClient

Client = rnc.FlareSolverrClient('.env.secret')

#Print Token
#print(Client.get_token())

#Account Data Test
Username = "Zigzatuzoo"
Success, json = RecNetClient.Accounts.GetAccountViaUsername(Client,Username)
print(json)

#Image Test
ImageID = '720425100'
Success, json = RecNetClient.Images.GetComments(Client,ImageID)

for i in json:
    print(i['PlayerId']," - ",i['Comment'])