# Rejurhf
# 12.10.2018

import json

json_data = {}
# json_data = 2
# json_data = '{{'
try:
    data = json.loads(json_data)
except (ValueError, TypeError) as e:
    print(type(e), e)
