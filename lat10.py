#if elif else:banyak kondisi
nilai = 78

if nilai >= 85:
    grade = "a"
elif nilai >= 70:
    grade = "b"
elif nilai >= 55:
    grade = "c"
else:
    grade = "d"

print(f"nilai {nilai} -> grade {grade}")