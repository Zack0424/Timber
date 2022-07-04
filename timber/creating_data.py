
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

print(names)
print(cities)
file_out = []
import random

for i in range(300):
    file_out.append([random.choice(names),random.choice(cities)])

with open("data_randomized.csv", "w",encoding="UTF-8") as f:
    for i in file_out:
        f.write(f"{';'.join(i)}\n")