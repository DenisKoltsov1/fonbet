import requests
token='3d7aabee89c348b084a80ce0cadb07be1014c43716464c07ab0670fafd464c8f'
headers = {'Authorization':token}
import requests
r = requests.get ('https://api.betting-api.com/1xbet/football/live/all', headers=headers)

print(r.json())