# batas = 5
# for i in range(batas):
#     print("ke -", i + 1)

# game = ["genshin", 7.0, True]
# for i in game:
#     print(i)

# nilai = [75, 60, 80, 60, 50]
# for item in nilai:
#     if item > 70:
#         print(item, "lulus")
#     else:
#         print("Tidak lulus")

# for i in range(5, 0, -1):
#     print(i)

# for i in range(1, 3):
#     for j in range(1, 4):
#         print(f'{i} x {j} = {i * j}')
#     print()

# jawab = "ya"
# hitung = 0
# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")

# print(f"Total Perulangan : {hitung}")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# n = int(input("masukan sejumlah perulangan: "))
# penghitung_ganjil = 0
# for i in range(1, n + 1):
#     if i % 2 == 1:
#         print(i)
#         penghitung_ganjil += 1
# print(f"banyak bilangan ganjil {penghitung_ganjil}")

uangSaku_awal = int(input("masukan jumlah uang saku awal: "))
uangSaku_akhir = uangSaku_awal
pengeluaran = int(input("masukan pengeluaran: "))
while pengeluaran <= uangSaku_awal:
    print(f'uang saku {uangSaku_awal} - {pengeluaran} = {uangSaku_akhir - pengeluaran}')
    uangSaku_akhir -= pengeluaran
    uangSaku_awal = uangSaku_akhir
    print(f'saldo sisa {uangSaku_akhir}')
    pengeluaran = int(input("Masukan pengeluaran: "))
print(f'saldo sisa: {uangSaku_akhir}')

buah = ["apel", "jeruk", "anggur"]
buah.append('mangga')
buah.insert(1, 'pisang')
buah.remove('jeruk')
print(buah[0])