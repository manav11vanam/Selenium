import json
from openpyxl import Workbook
wb = Workbook()
ws = wb.active

with open('data.txt') as f:
    s = f.readline().strip()
    # print(s)
    dictionary = json.loads(s)
    # print(dictionary)
    ws.append(list(dictionary.keys()))
    ws.append(list(dictionary.values()))
    for line in f:
        # print(line[:100])
        dictionary = json.loads(line)
        ws.append(list(dictionary.values()))
wb.save('Data.xlsx')
