import json
import time
from requests import get, post

# Endpoint URL
endpoint = r"https://formrecognizer-capture.cognitiveservices.azure.com"
# model_id = "db8da6ac-28ec-4c59-84ab-a63b6b01123e"
model_id = "81803696-5cde-456d-b2ca-a29d40c10dac"
includeKeys = 'True'
get_url = endpoint + "/formrecognizer/v2.0-preview/custom/models/%s/?includeKeys=%s" % (model_id, includeKeys)

headers = {
  'Ocp-Apim-Subscription-Key': '89ea53ef01c248b2a1c27db02afb4527'
}

try:
    resp = get(get_url, headers = headers)
    if resp.status_code != 200:
        print("GET model failed (%s):\n%s" %
              (resp.status_code, json.dumps(resp.json(), indent=2, sort_keys=True)))
        quit()
    print("GET model succeeded:\n%s" % json.dumps(resp.json(), indent=2, sort_keys=True))
except Exception as e:
    print("GET model failed:\n%s" % str(e))
    quit()