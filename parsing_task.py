import requests
import json
import csv
import itertools
import re

def generate_car_numbers():
    numbers = [f'{i:03}' for i in range(1, 1000)]
    letters2 = [''.join(p) for p in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=2)]
    letters3 = [''.join(p) for p in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=3)]
    suffixes = ['02']

    for number in numbers:
        for letter in letters2:
            for suffix in suffixes:
                yield f'{number}{letter}{suffix}'
        for letter in letters3:
            for suffix in suffixes:
                yield f'{number}{letter}{suffix}'

def parse_vehicle_info(car_number):
    url = 'https://apiv4.ffins.kz/v1/policy/searchvehicle'
    headers = {'Content-Type': 'application/json'}
    data = {'carnumber': car_number}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            result = response.json()
            car_model = result.get('carname')
            if car_model:
                # Replace all consecutive whitespace characters with a _
                car_model = re.sub(r'\s+', '_', car_model).strip()
                return car_model
            else:
                print(f"Model not found for car number {car_number}")
                return None
        else:
            print(f"Error retrieving data for car number {car_number}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    # Generate car numbers
    car_numbers = generate_car_numbers()

    # Prepare CSV file for writing
    csv_filename = 'car_models.csv'
    csv_header = ['Car_Number', 'Car_Model']

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_header)

        for car_number in car_numbers:
            car_model = parse_vehicle_info(car_number)
            if car_model is not None:
                writer.writerow([car_number, car_model])
                print(f"Processed: {car_number} | Car Model: {car_model}")
            else:
                print(f"Error processing: {car_number}")

    print(f"CSV file '{csv_filename}' created successfully.")

if __name__ == '__main__':
    main()
