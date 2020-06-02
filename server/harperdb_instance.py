import requests
import json

url = "https://conn-linguals-ConnectLinguals.harperdbcloud.com"

payload = "{\n  \"operation\": \"sql\",\n  \"sql\":\"SELECT topics FROM ConnectLinguals.topics\"\n}"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic amVuZWxsd2VpdHo6SGFycGVyaXNjb29sMDgzMSEh'
}

response = requests.request("POST", url, headers=headers, data=payload)
