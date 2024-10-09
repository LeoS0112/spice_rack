from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import json
from enum import Enum

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Spice(Enum):
    Cumin = 0
    Turmeric = 1

def getSpiceDict(spiceList: str):
    spiceDict = {Spice.Cumin: 0, Spice.Turmeric: 0}
    for i in range(len(spiceList)):
        spiceDict[Spice(i)] = int(spiceList[i])
    print(spiceDict)
    return spiceDict

@app.get("/spices/{spiceList}")
async def gen_spice_list(
        spiceList: str
):
    print(spiceList)
    current_spices = getSpiceDict(spiceList)
    return {"current spices:", str(list(current_spices.values()))}

