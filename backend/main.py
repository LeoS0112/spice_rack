import json
from enum import Enum

from flask import Flask

app = Flask(__name__)

class Spice(Enum):
    Basil = 0
    Oregano = 1
    Thyme = 2
    Herbes_De_Province = 3
    Marjoram = 4
    Tarragon = 5


def getSpiceDict(spiceList: str):
    spiceDict = {Spice.Cumin: 0, Spice.Turmeric: 0}
    for i in range(len(spiceList)):
        spiceDict[Spice(i)] = int(spiceList[i])
    print(spiceDict)
    return spiceDict

@app.route("/")
def homepage():
    return "Running"

@app.route('/spices/<string>')
def index(string):
    print(string)
    for i in range(5):
        if string[i] == 0:
            print(Spice[i].name)
    return string

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



