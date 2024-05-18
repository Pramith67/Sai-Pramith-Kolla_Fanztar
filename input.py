import requests
import json

url = "http://localhost:5000/order"
payload = {
    "components": ["I", "A", "D", "F", "K"]
}

response = requests.post(url, json=payload)

if response.status_code == 201:
    data = response.json()
    order_info = {
        "order_id": data['order_id'],
        "total_price": data['total'],
        "parts": data['parts']
    }
    print(response.status_code)
    print(json.dumps(order_info, indent=4))
else:
    error_info = {
        "error_code": response.status_code,
        "error_message": response.json().get('error')
    }
    print(json.dumps(error_info, indent=4))
