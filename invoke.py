import json
import requests
test_input = {
"data": "1257815,5, 1, 3, 1, 2, 2, 1, 1, 6, 4, 3, 2, 5, 5, 6, 5, 4, 4, 23, 6, 3, 2, 7, 8,8, 3, 2, 1, 6"
}
r = requests.post("https://9dvb7dwp18.execute-api.ca-central-1.amazonaws.com/product-churn/api-churn", data=json.dumps(test_input))
print(r.content)