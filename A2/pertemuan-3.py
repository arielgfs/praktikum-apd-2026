# angka = 6

# if angka < 10:
#     print("angka kurang dari 10")


# umur = int(input("Masukkan umur anda: "))
# if umur >= 17:
#     print("kamu sudah bisa membuat KTP")
# else:
#     print("kamu belum bisa membuat KTP")

# kendaraan = input("Masukkan jenis kendaraan: ").lower()

# if kendaraan == "mobil" or kendaraan == "Mobil":
#     tarif_parkir = 10000
# elif kendaraan == "motor" or kendaraan == "Motor":
#     tarif_parkir = 5000
# else:
#     tarif_parkir = 15000

# print("Tarif parkir yang harus dibayar", tarif_parkir)

# umur = 20
# status = "Dewasa" if umur >= 18 else "Belum Dewasa"
# print(status)

# nilai = int(input("Masukkan nilai anda: "))
# if nilai >= 10:
#     if nilai >= 20:
#         if nilai >= 30:
#             print("Angka besar")
#         print("Angka sedang")
#     print("Angka kecil")

# umur_pengunjung = int(input("Masukkan umur anda: "))

# status = "boleh masuk" if umur_pengunjung >= 16 else "Belum Dewasa"
# print(status)

total_belanja = int(input("Masukkan total belanja anda: "))
if total_belanja > 200000:
    total_belanja = total_belanja - (total_belanja * 0.3)
    print("yang harus dibayar adalah: ", total_belanja)
elif total_belanja > 100000:
    total_belanja = total_belanja - (total_belanja * 0.1)
    print("yang harus dibayar adalah: ", total_belanja)
else:
    print("tidak ada diskon, yang harus dibayar adalah: ", total_belanja) 
