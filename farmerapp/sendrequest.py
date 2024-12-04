import random
import requests

# Base URL of the API
BASE_URL = 'http://43.204.147.217/schedule'  # Replace with your actual base URL
HEADERS = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNDMwNjM1NCwianRpIjoiNzQ5NTM3NDEtZjgzZC00MWZiLWJkNGUtODJjMjE5NTQ1YmQwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VybmFtZSI6InN1cGVydXNlciIsInJvbGVzIjpbInN1cGVydXNlciJdfSwibmJmIjoxNzI0MzA2MzU0LCJjc3JmIjoiY2FmMTlmZGMtZjU1Zi00YWMwLWJhMDQtOWY1NGVkOWE5Njg3IiwiZXhwIjoxNzI0MzA5OTU0fQ.3Kj6eDD3MMzwKhMQXQZfMKsc05T7ZSQAL4ke5sksYvI'
}

# List of example fertilizers and units
fertilizers = ['Nitrogen', 'Phosphorus', 'Potassium', 'Urea', 'DAP']
quantity_units = ['kg', 'g', 'liters', 'ml']

# List of farm IDs to use for creating schedules
farm_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def create_schedule(days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id):
    url = f"{BASE_URL}/create-schedule"
    data = {
        'days_after_sowing': days_after_sowing,
        'fertiliser': fertiliser,
        'quantity': quantity,
        'quantity_unit': quantity_unit,
        'price_per_unit': price_per_unit,
        'farm_id': farm_id
    }
    response = requests.post(url, headers=HEADERS, json=data)
    return response.json(), response.status_code

for i in range(10):
    days_after_sowing = random.randint(1, 120)
    fertiliser = random.choice(fertilizers)
    quantity = round(random.uniform(1.0, 100.0), 2)
    quantity_unit = random.choice(quantity_units)
    price_per_unit = round(random.uniform(5.0, 50.0), 2)
    farm_id = random.choice(farm_ids)

    response, status = create_schedule(days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id)
    if status == 201:
        print(f"Successfully created schedule for farm ID {farm_id}")
    else:
        print(f"Failed to create schedule for farm ID {farm_id}, Status Code: {status}, Response: {response}")
