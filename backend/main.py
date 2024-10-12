import json
from enum import Enum
import time
from flask import Flask
import csv
import requests

url = "https://7103.api.greenapi.com/waInstance7103133296/sendMessage/f9f18859c9a54c7999b81998f957010043b8ce17d5044428ad"


Spice_Data_CSV_Path = "/home/leo/spice_data.csv"
app = Flask(__name__)

class Spice(Enum):
    Basil = 0
    Oregano = 1
    Thyme = 2
    Herbes_De_Province = 3
    Marjoram = 4
    Tarragon = 5
    Mixed_Herbs = 6
    Bay_Leaves = 7
    Garam_Masala = 8
    Cumin = 9
    Turmeric = 10
    Chilli_Powder = 11
    Paprika = 12
    Ginger = 13
    Mustard_Seeds = 14
    Nigella_Seeds = 15
    Chicken_Seasoning = 16
    Cajun_Seasoning = 17
    Crushed_Chillies = 18
    Garlic_Granules = 19
    Cinnamon_Sticks = 20
    Ground_Sweet_Cinnamon = 21
    Ground_Cinnamon = 22
    Star_Anise = 23

def getSpiceDict(spiceList: str):
    spiceDict = {Spice.Cumin: 0, Spice.Turmeric: 0}
    for i in range(len(spiceList)):
        spiceDict[Spice(i)] = int(spiceList[i])
    print(spiceDict)
    return spiceDict

def write_spice_data_to_csv(spice_list: str):
    current_time = time.time() # seconds after epoch
    with open(Spice_Data_CSV_Path, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, spice_list])

def read_last_line_spice_data_csv():
    with open(Spice_Data_CSV_Path, mode='r') as file:
        reader = csv.reader(file)
        for line in reader:
            last_line = line
    return last_line

def make_string(spices_changed, current_spices):
    to_return = ""
    for spice in spices_changed:
        if int(current_spices[spice.value]) == 0:
            to_return += Spice.name + " has been removed "
        else:
            to_return += Spice.name + " has been returned "
    return to_return

@app.route("/")
def homepage():
    return "Running"

@app.route('/spices/<string>')
def index(string):
    print("Current spices:" + string)
    for i in range(len(Spice)):
        if int(string[i]) == 0:
            print(Spice(i).name)
    last_row = read_last_line_spice_data_csv()
    last_row_spices = list(last_row[1])
    diff = list(i[0] == i[1] for i in zip(last_row_spices, list(string[:24])))
    spices_changed = list(Spice(i) for i in range(len(Spice)) if not diff[i])
    write_spice_data_to_csv(string)
    payload = {
        "chatId": "120363251450617955@g.us",
        "message": make_string(spices_changed, string[:24])
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=payload, headers=headers)
    return string

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





