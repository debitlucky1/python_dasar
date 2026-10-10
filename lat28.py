import csv

# 1. Muat data dari file CSV terlebih dahulu agar variabel 'data' terdefinisi
data = []
with open("nilai.csv", mode="r") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

# 2. Olah data (ambil d["nilai"] untuk rata-rata)
nilai = [d["nilai"] for d in data] 
rata = sum(nilai) / len(nilai)
print(f"rata-rata: {rata:.1f}")

# 3. Cari yang lulus
lulus = [d["nama"] for d in data if d["nilai"] >= 75]
print("lulus:", lulus)

# 4. Cari nilai tertinggi
top = max(data, key=lambda d: d["nilai"])
print("tertinggi:", top["nama"])