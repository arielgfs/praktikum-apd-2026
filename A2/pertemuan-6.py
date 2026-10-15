# # kartu = ["merah", "merah", "biru", "hijau"]
# # print(kartu)
# # set_kartu = set(kartu)
# # print(set_kartu)

# # for warna in set_kartu:
# #     print(warna)
# #     break

# # if warna == "merah":
# #     print("warna merah ada di set_kartu")
# # else:
# #     print("warna merah tidak ada di set_kartu")
# # set_kartu.add("kuning") 
# # print(set_kartu)

# # set_kartu.discard("biru")
# # print(set_kartu)
# # for i in set_kartu:
# #     print(i)

# Biodata = {
#     "Nama" : "Siti Julpa",
#     "NIM" : 25091060,
#     "KRS" : ["Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" : True,
#     "Instagram" : "julpatarr"
# }

# print(Biodata)
# print(Biodata["Nama"])
# print(Biodata["KRS"][1])
# print(Biodata.get("NIM"))
# print(Biodata.get("TEST"))
# print()

# for i in Biodata:
#     print(Biodata[i])

# poli_umum = {"Andi", "Budi", "Citra", "Doni"}
# poli_gigi = {"Citra", "Doni", "Eka", "Fani"}
# daftar_pasien = poli_umum.union(poli_gigi)
# print(daftar_pasien)

produk = {
    1: {"nama": "buku", "harga": 5000, "stok": 10},
    2: {"nama": "pensil", "harga": 2000, "stok": 5}
}

for key, value in produk.items():
    print(f"produk ke-{key}:")
    for key_dalam, value_dalam in value.items():
        print(f"{key_dalam}: {value_dalam}")
    print()