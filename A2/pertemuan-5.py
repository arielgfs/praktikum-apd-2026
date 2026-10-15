# nama1 = "Attar"
# nama2 = "Johan"
# nama3 = "Azka"

# print(nama1, nama2, nama3)

# list_nama = ["Attar", "Johan", "Azka"]
# list_nama.append("julpa") #menambahkan data di akhir list
# print(list_nama)

# print(list_nama[:2])
# for i in list_nama:
#     print(i)

# #menambahkan elemen di list
# list_nama.extend(["mirza", "wili"]) #ibarat menambahkan list ke list
# print(list_nama)

# list_nama.insert(1, "mustafid") #menambahkan data di index tertentu
# print(list_nama)

# list_nama[0:3] = ["hafiz", "dewi", "meisya"] #mengubah data di index tertentu
# print(list_nama)

# #menghapus elemen di list
# del list_nama[1] #menghapus data di index tertentu
# print(list_nama)

# list_nama.remove("meisya") #menghapus data tertentu
# print(list_nama)

# ambil_nama = list_nama[:1] #bisa menghapus dan mengambil data sekaligus
# print(list_nama)
# print(ambil_nama)

# poin1 = [1, 2, 3, 4, 5, 6, 7]
# poin2 = [8, 9, 10]
# poin = poin2 * 3
# print(poin)
# #mengubah 5, 6, 7, menjadi 11, 12, 13
# poin[4:7] = [11, 12, 13]
# print(poin[1:5:2]) #mengambil data dari index 1 sampai 5 dengan step 2

# line_up = [
#     ["Ferrari", "Leclerc", 16],
#     ["Mercedes", "Hamilton", 44],
#     ["Red Bull", "Verstappen", 1],
#     ["McLaren", "Norris", 4]
# ]
# print(line_up[2][1])

# for i in line_up:
#     for j in i:
#         print(j, end=" ")
#     print()

#TUPLE
# nama = ("apel", "mangga", "nanas")
# print(nama)



# data_harian = ["Senin", 36.5, "Selasa", 37.1, "Rabu", 36.8, "Kamis", 37.0, "Jumat", 36.6]
# print(data_harian[1:10:2])

# profil_karakter = ("Arthur", 50, True, ["Pedang Suci", "Tameng Naga"])
# list_profil = []
# for i in profil_karakter[::-1]:
#     list_profil.extend([i])
# profil_karakter = tuple(list_profil)
# print(profil_karakter)

nama = ["Attar", "Johan", "gin"]
role = ["Admin", "User", "User"]
gender = ["Laki-laki", "Laki-laki", "Perempuan"]

for i in range(len(nama)):
    if gender[i] == "Laki-laki" and role[i] == "Admin":
        print(nama[i])
