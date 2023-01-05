import jsonpath
import json
import requests
with open("manifest.json") as Url:
    url=json.load(Url)

with open("data_create_user.json", "r") as file:
    json_input=file.read()
    request_json=json.loads(json_input)
response =requests.post(url['URL'],request_json)
try:
    assert response.status_code ==201
    print("Success")
except Exception as e:
    print(e)
header=response.headers

content_lengt =response.headers.get('Content-Length')

request_json = json.loads(response.text)

print("Result Request: ",request_json)

with open("result.json","w") as result:
    result1=json.dumps(request_json)
    result.write(result1)

