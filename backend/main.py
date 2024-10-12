import json
from enum import Enum

from flask import Flask

app = Flask(__name__)

class Spice(Enum):
    Cumin = 0
    Turmeric = 1

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
    return string

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



