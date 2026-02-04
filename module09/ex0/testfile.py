from correct_dt_space_station import SPACE_STATIONS
from ex0.space_station import SpaceStation

try:
    for data in SPACE_STATIONS:
        obj = SpaceStation(**data)
except:
    print("Somthing went wrong")
