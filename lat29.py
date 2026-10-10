import csv

# 1. Muat data dari file CSV terlebih dahulu agar variabel 'data' terdefinisi
data = []
with open("nilai.csv", mode="r") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

# 2. Rekap nilai per kelas
rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'kelas':<6}{'jumlah':>8}{'rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")