from bs4 import BeautifulSoup
import requests
import urllib.parse
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

requirements = ['Variant', 'Seating Capacity', 'Doors', 'Body Type', 'Cylinder Configuration', 'Cylinders', 'Valves Per Cylinder', 'Displacement', 'Power', 'Torque', 'Compression Ratio', 'Engine Location', 'Fuel System', 'Fuel Type', 'City Mileage', 'Highway Mileage', 'ARAI Certified Mileage', 'Emission Norm', 'Drivetrain', 'Gears', 'Type', 'Front Brakes', 'Rear Brakes', 'Front Suspension', 'Rear Suspension', 'Front Tyre & Rim', 'Rear Tyre & Rim', 'Wheels Size', 'Handbrake', 'Number of Airbags', 'Airbags', 'Engine Immobilizer', 'Parking Assistance', 'Child Safety Locks', 'Auto-Dimming Rear-View Mirror', 'Door Ajar Warning', 'ISOFIX (Child-Seat Mount)', 'Central Locking', 'ABS (Anti-lock Braking System)', 'EBD (Electronic Brake-force Distribution)', 'EBA (Electronic Brake Assist)', 'Power Windows', 'Power Steering', 'Instrument Console', 'Multifunction Display', 'Adjustable Steering Column', 'Seats Material', 'Sun Visor', 'Clock', 'Audiosystem', 'Ventilation System', 'Boot-lid Opener', 'Fuel-lid Opener', '12v Power Outlet', 'Third Row AC Vents', 'Adjustable Headrests', 'CD / MP3 / DVD Player', 'FM Radio', 'Bluetooth', 'USB Compatibility', 'Aux-in Compatibility', 'Cup Holders', 'Door Pockets', 'Seat Back Pockets', 'Keyless Entry', 'Tachometer', 'Odometer', 'Average Fuel Consumption', 'Gear Shift Reminder', 'Average Speed', 'Tripmeter', 'Distance to Empty', 'Fuel Gauge', 'Engine Malfunction Light', 'Speedometer', 'Key Off Reminder', 'Headlight Reminder', 'Low Fuel Warning', 'Fasten Seat Belt Warning', 'Basic Warranty', 'Extended Warranty', 'Length', 'Width', 'Height', 'Wheelbase', 'Front Track', 'Rear Track', 'Ground Clearance', 'Kerb Weight', 'Gross Vehicle Weight', 'Boot Space', 'Fuel Tank Capacity', 'Minimum Turning Radius']

url = 'https://autoportal.com/newcars/marutisuzuki/swift/'
res = requests.get(url)
html = res.content
soup = BeautifulSoup(html, 'lxml')

list_div = soup.find('div', class_='breadcrumbs')
list_items = list_div.find('ul').find_all('li')
brand = list_items[-2].text.strip()
model = list_items[-1].text.strip().replace(brand + ' ', '')
final_dict = {'Brand': brand, 'Model': model}

headers = list(final_dict.keys()) + requirements
ws.append(headers)

specs_link = soup.find('a', {'class': 'item', 'data-trackevent-action': "SpecificationsFeatures"})
specs_link = specs_link.get('href')
specs_link = urllib.parse.urljoin(url, specs_link)

''' Get the First Specs Page of the Vehicle '''
res = requests.get(specs_link)
html = res.content
soup = BeautifulSoup(html, 'lxml')

''' Find all the available variants in the page'''
select = soup.find('select', {'class': 'field', 'name': 'variant_key'})
options = select.find_all('option')
variants = []

header_flag = 1
for option in options:
    variants.append(option.get('value'))
    # print(option.get('value'))

''' Fetch the details of each variant and print it'''
for variant in variants:
    payload = {'variant_key': variant}
    res = requests.post(specs_link, payload)
    soup = BeautifulSoup(res.content, 'lxml')

    specs_heading = soup.find('div', class_='spec-resume').p.text # Name of the variant
    full_name = specs_heading[specs_heading.find(model):]

    table_divs = soup.find_all('div', class_='spec-list')
    model_dict = {'Variant': full_name}
    for table_div in table_divs:
        rows = table_div.find_all('div', class_='row item')
        for row in rows:
            features = row.find_all('div')
            if len(features) == 1: continue
            k, v = features[0].text.strip(), features[1].text.strip()
            model_dict[k] = v

    for requirement in requirements:
        try:
            # final_dict[requirement] = int(model_dict.get(requirement, 'N/A'))
            value = model_dict.get(requirement, 'N/A')
            value = value.replace(' cc', '')
            value = value.replace(' km/litre', '')
            value = value.replace(' mm', '')
            value = value.replace(' kg', '')
            value = value.replace(' litres', '')

            final_dict[requirement] = int(value)
        except ValueError:
            final_dict[requirement] = model_dict.get(requirement, 'N/A')

    # final_dict['Power'] = int(final_dict['Power'][:final_dict['Power'].find('PS')]) // 1.36

    # if header_flag:
    #     headers = list(final_dict.keys()) # + requirements
    #     ws.append(headers)
    #     header_flag = 0

    for k, v in final_dict.items():
        print(f'{k}: {v}')

    ws.append(list(final_dict.values()))
    # ws.append(list(model_dict.values()))
    print('*'*50)

wb.save('Cars_test_scraper.xlsx')
