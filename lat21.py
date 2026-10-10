#lambda.py
kuadrat = lambda x: x ** 2
print(kuadrat(4))

siswa = [("ani", 80), ("budi", 95)]
print(max(siswa, key=lambda s: s[1]))

#scope.py
x = "global"
def tes():
    x = "lokal"     #hanya didalam tes()
    print(x)        #lokal
tes()
print(x)            #global