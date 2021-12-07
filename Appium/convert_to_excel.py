import json
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
fname = 'data_for_emissions.txt'
with open(fname) as f:
    headers = ['Owner Name', 'Ownership (Serial No)', 'Registration No', 'Maker Model', 'Vehicle Class', 'Engine  No.', 'Chassis No.', 'Fuel Type', 'Fuel Norms', 'Registration Date', 'Unloaded Weight (Kg)']
    ws.append(headers)
    for line in f:
        # print(line[:100])
        dictionary = json.loads(line)
        # if not dictionary['Registration No'].startswith('MH12'):
        #     continue
        try:
            dictionary['Unloaded Weight (Kg)'] = int(dictionary['Unloaded Weight (Kg)'])
        except ValueError:
            dictionary['Unloaded Weight (Kg)'] = dictionary['Unloaded Weight (Kg)']
        ws.append(list(dictionary.values()))
wb.save(fname.replace('txt', 'xlsx'))
