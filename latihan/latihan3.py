test_case = [
    "Nilai siswa valid",
    "Nilai siswa bernilai 0",
    "Nilai siswa bernilai 100",
    "Nilai siswa di bawah 0",
    "Nilai siswa di atas 100",
    "Nilai siswa berupa huruf"
]

print("DAFTAR TEST CASE")
for nomor, kasus in enumerate(test_case, start=1):
    print(f"{nomor}. {kasus}")