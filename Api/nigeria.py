import requests
import pandas as pd

state = []
latitude = []
longitude = []
response = requests.get("https://nigeria-states-towns-lga.onrender.com/api/states")

length = (len(response.json()))
for i in range(0, length):
    state.append(response.json()[i]['state_code'])
    latitude.append(response.json()[i]['location']['latitude'])
    longitude.append(response.json()[i]['location']['longitude'])

diction = {"state": state, "latitude": latitude, "longitude": longitude}
df = pd.DataFrame(diction)
print(df.info())
df.to_csv("nigeria_states.csv")