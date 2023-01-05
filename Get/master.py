import json

import requests
with open('manifest.json') as urL:
    url=json.load(urL)


response =requests.get(url['URL'])
try:
    assert response.status_code ==201
    print("Success")
except Exception as e:
    print(e)
header=response.headers

content_lengt =response.headers.get('Content-Length')

request_json = json.loads(response.text)

print("Result Request: ",request_json)

with open("result.json","w")as result:
   result1=json.dumps(request_json)
   result.write(result1)
