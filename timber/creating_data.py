
names = []
cities = []
with open("data_to_be_randomized\male_names.csv") as f:
    for i in f:
        i = i.strip()
        names.append(i)

with open("data_to_be_randomized/female_names.csv") as f:
    for i in f:
        i = i.strip()
        names.append(i)


with open("data_to_be_randomized/cities.csv", encoding="UTF-8") as f:
    for i in f:
        i = i.strip()
        if i != "":
            cities.append(i)

mf = ["male","female"]


file_out = []
from geopy.geocoders import Nominatim
from geopy.point import Point
import random

for i in range(300):
    try:
        random_city = random.choice(cities)
        locator = Nominatim(user_agent="test")
        place = locator.geocode(random_city)
        file_out.append([str(i),random.choice(names),random_city,str(place.latitude), str(place.longitude), random.choice(mf), random.choice(mf)])
        with open(f'users\{i}.txt','w') as f:
            pass
    except Exception:
        print("oops")
with open("data_randomized.csv", "w",encoding="UTF-8") as f:
    for i in file_out:
        f.write(f"{';'.join(i)}\n")