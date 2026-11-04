"""CREATE: menambah game, user, dan pesanan."""
import storage
from storage import cari_nama, hitung_subtotal


def tambah_game():
    nama_game = input("Masukkan nama game: ")
    genre_game = input("Masukkan genre game: ")
    harga_game = int(input("Masukkan harga game: "))
    stok_game = int(input("Masukkan stok game: "))

    if nama_game not in storage.game:
        storage.game[nama_game] = {
            "genre": genre_game,
            "harga": harga_game,
            "stok": stok_game
        }
        print("Game berhasil ditambahkan")
    else:
        print("Nama game sudah tersedia")


def tambah_user():
    nama_user = input("Masukkan nama user baru: ")
    password_user = input("Masukkan password user baru: ")
    role_user = input("Masukkan role user baru (admin/petugas): ")

    if role_user != "admin" and role_user != "petugas":
        print("Role tidak valid")
    elif nama_user in storage.user:
        print("Nama user sudah digunakan")
    else:
        storage.user[nama_user] = {
            "password": password_user,
            "role": role_user
        }
        print("User berhasil ditambahkan")


def tambah_pesanan():
    nomor = int(input("Pilih nomor game yang ingin dipesan: "))
    nama_game = cari_nama(storage.game, nomor)

    if nama_game == "":
        print("Nomor game tidak valid")
        return

    jumlah = int(input("Masukkan jumlah game yang ingin dipesan: "))

    if jumlah > 0 and jumlah <= storage.game[nama_game]["stok"]:
        genre_game = storage.game[nama_game]["genre"]
        harga_game = storage.game[nama_game]["harga"]
        subtotal = hitung_subtotal(harga_game, jumlah)

        storage.game[nama_game]["stok"] -= jumlah

        nomor_baru = storage.counter["nomor_pesanan_baru"]
        storage.pemesanan[nomor_baru] = {
            "nama": nama_game,
            "genre": genre_game,
            "harga": harga_game,
            "jumlah": jumlah,
            "subtotal": subtotal
        }
        storage.counter["nomor_pesanan_baru"] += 1

        print("Pesanan berhasil ditambahkan")
        print("Sisa stok:", storage.game[nama_game]["stok"])
    else:
        print("Stok tidak cukup atau jumlah tidak valid")
        print("Pesanan tidak ditambahkan")
