import requests
import json

client_id = "sb-6490bec8-2aa2-491d-b03e-47a885faf58b!b217731|aicore!b540"
client_secret = "273eac8b-a2b2-4fa4-9f21-ee0b7f9a4060$5VWVeayFNaVjuFVK-GZCxcGT3VeOlHoA6MHV1IHuh7g="

grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}

url="https://ishsapbuild.authentication.eu10.hana.ondemand.com" + "/oauth/token"
response = requests.post(url, data=body_params, auth = (client_id, client_secret)) 

token_raw = json.loads(response.text)
token = token_raw["access_token"]

headers = {"Authorization": "Bearer {}".format(token), "AI-Resource-Group" : "default"}

r = requests.post(url="https://api.ai.prod.eu-central-1.aws.ml.hana.ondemand.com/v2/inference/deployments/d871605f17b059f2/v2/predict", json=body,headers=headers)
print(r.text)
