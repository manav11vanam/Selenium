from bs4 import BeautifulSoup
import requests
import json
import threading

def get_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')

    tables = soup.find_all('table')
    rows = []
    for table in tables:
        rows.extend(table.find_all('tr'))

    cd = {}
    for row in rows:
        tds = row.find_all('td')
        if len(tds) != 2: continue
        cd[tds[0].text] = tds[1].text

    print(cd)
    requirements = ['Engine Displacement', 'Maximum Power', 'Maximum Torque', 'Gearbox', 'Ground Clearance', 'Kerb Weight', 'Boot Space', 'Fuel Tank Capacity', 'Car Variant', 'Current Status', 'Body Type', 'Fuel Type', 'Shades', 'Transmission Type', 'Engine Description', 'No. of Cylinders', 'No. of Valves', 'Emission Standard', 'Valvetrain Type', 'Overall Length', 'Overall Width', 'Overall Height', 'Wheelbase', 'Seating Capacity', 'Number of Seating Rows', 'Number of Doors', 'Front Tyre', 'Rear Tyre', 'Wheels', 'Spare Wheel']

    final_dict = {}
    for requirement in requirements:
        final_dict[requirement] = cd.get(requirement, 'NA')

    with open('company.json', 'a') as f:
        s = json.dumps(final_dict)
        f.write(s + '\n')

if __name__ == "__main__":
    # url = 'https://autos.maxabout.com/cars/hyundai/santro/santro-new'
    with open('links.txt') as f:
        urls = f.readlines()

    urls = list(map(str.strip, urls))

    threads = []
    for url in urls:
        t = threading.Thread(target=get_data, args=[url])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
    # get_data(url)
