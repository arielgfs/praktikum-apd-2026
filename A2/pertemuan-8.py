# import inquirer
# # Menyusun daftar pertanyaan menu
# pertanyaan = [
#     inquirer.List(
#         "menu",
#         message="Pilih menu aplikasi",
#         choices=["Tambah Data", "Lihat Data", "Keluar"],
#     ),
# ]
# # Menampilkan prompt di terminal dan menyimpan hasil pilihan
# jawaban = inquirer.prompt(pertanyaan)
# print(jawaban)
# print(jawaban["menu"]) # Mengambil nilai berdasarkan key 'menu': Tambah Data

# import random
# cowo = input("masukan nama cowo: ")
# cewe = input("masukan nama cewe: ")
# ketentuan = random.randint(1, 2)
# if ketentuan == 1:
#     nilai = random.randint(1, 79)
# if ketentuan == 2:
#     nilai = random.randint(80, 100)
# print(f"Nilai kecocokan antara {cowo} dan {cewe} adalah {nilai}%")
import random
print("pencari inisial jodoh")
inisial = "abcdefghijklmnopqrstuvwxyz"
masukan = input("masukan nama anda: ")
jodoh = random.choice(inisial)
print(f"inisial jodoh anda adalah {jodoh}")