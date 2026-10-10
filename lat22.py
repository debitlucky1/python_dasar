#eror handling try except.py
try:
    angka = int(input("masukan angka: "))
    hasil = 100 / angka
except ValueError:
    print("harus berupa angka!")
except ZeroDivisionError:
    print("tidak bisa dibagi nol!")
else:
    print(f"hasil: {hasil}")
finally:
    print("selesai.")