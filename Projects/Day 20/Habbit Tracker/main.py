import requests
from datetime import datetime

user_name = "preettaparia"
token_name = "ad9hqoanspd0-qk"
graph_name = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : token_name,
    "username" : user_name,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

#respose = requests.post(url = pixela_endpoint, json = user_params)
#print(respose.text)

graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"

graph_config = {
    "id" : graph_name,
    "name" : "Coding",
    "unit" : "Hour",
    "type" : "float",
    "color" : "kuro",
}

headers = {
    "X-USER-TOKEN" : token_name
}

# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph_name}"

today = datetime(year=2023, month=7, day=3)

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "5.3",
    
}

response = requests.post(url = pixel_creation_endpoint, json = pixel_data, headers=headers)
print(response.text)
