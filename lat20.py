#jenis parameter argumen.py
def sapa(nama, salam="halo"):
    return f"{salam}, {nama}!"

print(sapa("ani"))
print(sapa(salam="hai", nama="budi"))

def total(*angka):
    return sum(angka)

print(total(1, 2, 3, 4))