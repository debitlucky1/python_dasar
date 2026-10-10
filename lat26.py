#baca data csv.py
import csv

data = []
with open("nilai.csv", mode="r") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

print(len(data), "baris")

if len(data) > 2:
    print(data[2])
else:
    print("data kurang dari 3 elemen!")