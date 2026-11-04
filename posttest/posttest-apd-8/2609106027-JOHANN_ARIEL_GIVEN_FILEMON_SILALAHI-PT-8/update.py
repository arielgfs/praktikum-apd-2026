"""UPDATE: mengedit game, user, dan pesanan."""
import storage
from storage import cari_nama, hitung_subtotal


def edit_game():
    nomor = int(input("Masukkan nomor game yang ingin diedit: "))
    nama_lama = cari_nama(storage.game, nomor)

    if nama_lama == "":
        print("Nomor game tidak valid")
        return

    nama_game = input("Masukkan nama game baru: ")
    genre_game = input("Masukkan genre game baru: ")
    harga_game = int(input("Masukkan harga game baru: "))
    stok_game = int(input("Masukkan stok game baru: "))

    stok_dipesan = 0
    for no_pesanan in storage.pemesanan:
        if storage.pemesanan[no_pesanan]["nama"] == nama_lama:
            stok_dipesan += storage.pemesanan[no_pesanan]["jumlah"]

    if stok_game >= stok_dipesan and (
        nama_game == nama_lama or nama_game not in storage.game
    ):
        storage.game[nama_game] = {
            "genre": genre_game,
            "harga": harga_game,
            "stok": stok_game - stok_dipesan
        }

        if nama_game != nama_lama:
            del storage.game[nama_lama]

        for no_pesanan in storage.pemesanan:
            if storage.pemesanan[no_pesanan]["nama"] == nama_lama:
                storage.pemesanan[no_pesanan]["nama"] = nama_game
                storage.pemesanan[no_pesanan]["genre"] = genre_game

        print("Game berhasil diedit")
    else:
        print("Nama game sudah digunakan atau stok tidak valid")


def edit_user():
    nomor = int(input("Masukkan nomor user yang ingin diedit: "))
    nama_lama = cari_nama(storage.user, nomor)

    if nama_lama == "":
        print("Nomor user tidak valid")
        return

    nama_user = input("Masukkan nama user baru: ")
    password_user = input("Masukkan password user baru: ")
    role_user = input("Masukkan role user baru (admin/petugas): ")

    if role_user != "admin" and role_user != "petugas":
        print("Role tidak valid")
    elif nama_user != nama_lama and nama_user in storage.user:
        print("Nama user sudah digunakan")
    else:
        storage.user[nama_user] = {
            "password": password_user,
            "role": role_user
        }

        if nama_user != nama_lama:
            del storage.user[nama_lama]

        print("User berhasil diedit")


def edit_pesanan():
    if len(storage.pemesanan) == 0:
        print("Belum ada pesanan")
        return

    nomor = int(input("Masukkan nomor pesanan yang ingin diedit: "))
    nomor_pesanan = cari_nama(storage.pemesanan, nomor)

    if nomor_pesanan == "":
        print("Nomor pesanan tidak valid")
        return

    pesanan = storage.pemesanan[nomor_pesanan]
    nama_game = pesanan["nama"]

    print("Nama game:", nama_game)
    print("Harga lama:", pesanan["harga"])
    print("Jumlah lama:", pesanan["jumlah"])

    if nama_game not in storage.game:
        print("Game tidak ditemukan")
        return

    jumlah_lama = pesanan["jumlah"]
    harga_baru = int(input("Masukkan harga baru: "))
    jumlah_baru = int(input("Masukkan jumlah baru: "))

    # Kembalikan stok lama dulu, lalu cek apakah jumlah baru cukup
    storage.game[nama_game]["stok"] += jumlah_lama

    if (
        harga_baru >= 0
        and jumlah_baru > 0
        and jumlah_baru <= storage.game[nama_game]["stok"]
    ):
        storage.game[nama_game]["stok"] -= jumlah_baru

        pesanan["harga"] = harga_baru
        pesanan["jumlah"] = jumlah_baru
        pesanan["subtotal"] = hitung_subtotal(harga_baru, jumlah_baru)

        print("Pesanan berhasil diedit")
        print("Sisa stok:", storage.game[nama_game]["stok"])
    else:
        storage.game[nama_game]["stok"] -= jumlah_lama
        print("Harga atau jumlah tidak valid")
        print("Pesanan tidak diubah")
