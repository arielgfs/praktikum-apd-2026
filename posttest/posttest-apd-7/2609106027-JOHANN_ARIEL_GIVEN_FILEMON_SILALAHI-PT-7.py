import os

user = {
    "admin": {"password": "admin123", "role": "admin"},
    "johann": {"password": "johann123", "role": "petugas"}
}

game = {
    "God Of War": {"genre": "Action", "harga": 500000, "stok": 3},
    "FIFA 23": {"genre": "Sport", "harga": 400000, "stok": 5},
    "GTA V": {"genre": "Action", "harga": 300000, "stok": 2},
    "The Sims 4": {"genre": "Simulation", "harga": 200000, "stok": 4},
    "Minecraft": {"genre": "Adventure", "harga": 250000, "stok": 6}
}

pemesanan = {}
nomor_pesanan_baru = 1
program_status = True

def cari_nama(data, nomor):
    hasil = ""
    i = 1

    for nama_item in data:
        if i == nomor:
            hasil = nama_item
        i += 1

    return hasil

def hitung_subtotal(harga, jumlah):
    subtotal = harga * jumlah
    return subtotal


def ambil_menu():
    pilihan = int(input("Masukkan menu yang dipilih: "))
    return pilihan

def hitung_total_harga():
    total = 0
    for nomor in pemesanan:
        total += pemesanan[nomor]["subtotal"]
    return total

def tampilkan_game():
    print("\nDAFTAR GAME")
    print("No | Nama game | Genre | Harga | Stok")

    i = 1
    for nama_game in game:
        print(
            i, "|", nama_game, "|",
            game[nama_game]["genre"], "|",
            "Rp.", game[nama_game]["harga"], "|",
            game[nama_game]["stok"]
        )
        i += 1

def cetak_struk():
    print("\n========== STRUK PEMBELIAN ==========")

    for nomor in pemesanan:
        print("Nama game:", pemesanan[nomor]["nama"])
        print("Harga: Rp.", pemesanan[nomor]["harga"])
        print("Jumlah:", pemesanan[nomor]["jumlah"])
        print("Subtotal: Rp.", pemesanan[nomor]["subtotal"])
        print("-------------------------------------")

    print("Total harga: Rp.", hitung_total_harga())
    print("=====================================")


while program_status == True:
    login_count = 3
    login_berhasil = False

    while login_count > 0 and login_berhasil == False:
        print("\n========== LOGIN ==========")
        nama = input("Masukkan nama user: ")
        password = input("Masukkan password user: ")

        login_count -= 1
        role = ""

        if nama in user and password == user[nama]["password"]:
            login_berhasil = True
            role = user[nama]["role"]

        if login_berhasil == True:
            print("\nLogin berhasil")
            print("Selamat datang", nama)
            print("Role anda adalah", role)
        else:
            print("Nama user atau password salah")
            if login_count > 0:
                print("Login tersisa:", login_count, "kali")

    if login_berhasil == False:
        print("\nKesempatan login habis")
        print("Program dihentikan")
        break

    logout = False

    if role == "admin":
        while program_status == True and logout == False:
            tampilkan_game()

            print("\nDAFTAR USER")
            print("No | Nama user | Password | Role")

            i = 1
            for nama_user in user:
                print(
                    i, "|", nama_user, "|",
                    user[nama_user]["password"], "|",
                    user[nama_user]["role"]
                )
                i += 1

            print("""
Pilih menu:
1. Tambah Game
2. Edit Game
3. Hapus Game
4. Tambah User
5. Edit User
6. Logout
7. Keluar dari Program
            """)
            try:
                input_menu = ambil_menu()

                if input_menu == 1:
                    nama_game = input("Masukkan nama game: ")
                    genre_game = input("Masukkan genre game: ")
                    harga_game = int(input("Masukkan harga game: "))
                    stok_game = int(input("Masukkan stok game: "))

                    if nama_game not in game:
                        game[nama_game] = {
                            "genre": genre_game,
                            "harga": harga_game,
                            "stok": stok_game
                        }
                        print("Game berhasil ditambahkan")
                    else:
                        print("Nama game sudah tersedia")

                elif input_menu == 2:
                    edit_game = int(
                        input("Masukkan nomor game yang ingin diedit: ")
                    )

                    nama_lama = cari_nama(game, edit_game)

                    if nama_lama != "":
                        nama_game = input("Masukkan nama game baru: ")
                        genre_game = input("Masukkan genre game baru: ")
                        harga_game = int(input("Masukkan harga game baru: "))
                        stok_game = int(input("Masukkan stok game baru: "))

                        stok_dipesan = 0

                        for nomor in pemesanan:
                            if pemesanan[nomor]["nama"] == nama_lama:
                                stok_dipesan += pemesanan[nomor]["jumlah"]

                        if (
                            stok_game >= stok_dipesan
                            and (
                                nama_game == nama_lama
                                or nama_game not in game
                            )
                        ):
                            game[nama_game] = {
                                "genre": genre_game,
                                "harga": harga_game,
                                "stok": stok_game - stok_dipesan
                            }

                            if nama_game != nama_lama:
                                del game[nama_lama]

                            for nomor in pemesanan:
                                if pemesanan[nomor]["nama"] == nama_lama:
                                    pemesanan[nomor]["nama"] = nama_game
                                    pemesanan[nomor]["genre"] = genre_game

                            print("Game berhasil diedit")
                        else:
                            print("Nama game sudah digunakan atau stok tidak valid")
                    else:
                        print("Nomor game tidak valid")

                elif input_menu == 3:
                    hapus_game = int(
                        input("Masukkan nomor game yang ingin dihapus: ")
                    )

                    nama_dihapus = cari_nama(game, hapus_game)

                    if nama_dihapus != "":
                        ada_pesanan = False

                        for nomor in pemesanan:
                            if pemesanan[nomor]["nama"] == nama_dihapus:
                                ada_pesanan = True

                        if ada_pesanan == False:
                            del game[nama_dihapus]
                            print("Game berhasil dihapus")
                        else:
                            print("Game tidak bisa dihapus karena masih ada pesanan")
                    else:
                        print("Nomor game tidak valid")

                elif input_menu == 4:
                    nama_user = input("Masukkan nama user baru: ")
                    password_user = input("Masukkan password user baru: ")
                    role_user = input("Masukkan role user baru (admin/petugas): ")

                    if role_user == "admin" or role_user == "petugas":
                        if nama_user not in user:
                            user[nama_user] = {
                                "password": password_user,
                                "role": role_user
                            }
                            print("User berhasil ditambahkan")
                        else:
                            print("Nama user sudah digunakan")
                    else:
                        print("Role tidak valid")

                elif input_menu == 5:
                    edit_user = int(
                        input("Masukkan nomor user yang ingin diedit: ")
                    )

                    nama_lama = cari_nama(user, edit_user)

                    if nama_lama != "":
                        nama_user = input("Masukkan nama user baru: ")
                        password_user = input("Masukkan password user baru: ")
                        role_user = input("Masukkan role user baru (admin/petugas): ")

                        if role_user == "admin" or role_user == "petugas":
                            if nama_user == nama_lama or nama_user not in user:
                                user[nama_user] = {
                                    "password": password_user,
                                    "role": role_user
                                }

                                if nama_user != nama_lama:
                                    del user[nama_lama]

                                print("User berhasil diedit")
                            else:
                                print("Nama user sudah digunakan")
                        else:
                            print("Role tidak valid")
                    else:
                        print("Nomor user tidak valid")

                elif input_menu == 6:
                    logout = True
                    os.system("cls")
                    print("Logout berhasil")

                elif input_menu == 7:
                    program_status = False
                    os.system("cls")
                    print("Program selesai. Terima kasih!")

                else:
                    print("Menu tidak valid")
            except ValueError:
                print("Input yang anda masukkan bukan Integer (angka)")

    elif role == "petugas":
        while program_status == True and logout == False:
            tampilkan_game()

            print("\nDAFTAR PESANAN")
            print("No | Nama game | Genre | Harga | Jumlah | Subtotal")

            i = 1
            for nomor in pemesanan:
                print(
                    i, "|",
                    pemesanan[nomor]["nama"], "|",
                    pemesanan[nomor]["genre"], "|",
                    "Rp.", pemesanan[nomor]["harga"], "|",
                    pemesanan[nomor]["jumlah"], "|",
                    "Rp.", pemesanan[nomor]["subtotal"]
                )
                i += 1

            print("""
Pilih menu:
1. Tambah Pesanan
2. Edit Pesanan
3. Hapus Pesanan Berdasarkan Nomor Pesanan
4. Hapus Seluruh Pesanan
5. Print Struk
6. Logout
7. Keluar dari Program
            """)
            try:
                input_menu = ambil_menu()

                if input_menu == 1:
                    pesanan_baru = int(
                        input("Pilih nomor game yang ingin dipesan: ")
                    )

                    nama_game = cari_nama(game, pesanan_baru)

                    if nama_game != "":
                        jumlah = int(
                            input("Masukkan jumlah game yang ingin dipesan: ")
                        )

                        if jumlah > 0 and jumlah <= game[nama_game]["stok"]:
                            genre_game = game[nama_game]["genre"]
                            harga_game = game[nama_game]["harga"]
                            subtotal = hitung_subtotal(harga_game, jumlah)

                            game[nama_game]["stok"] -= jumlah

                            pemesanan[nomor_pesanan_baru] = {
                                "nama": nama_game,
                                "genre": genre_game,
                                "harga": harga_game,
                                "jumlah": jumlah,
                                "subtotal": subtotal
                            }

                            nomor_pesanan_baru += 1

                            print("Pesanan berhasil ditambahkan")
                            print("Sisa stok:", game[nama_game]["stok"])
                        else:
                            print("Stok tidak cukup atau jumlah tidak valid")
                            print("Pesanan tidak ditambahkan")
                    else:
                        print("Nomor game tidak valid")

                elif input_menu == 2:
                    if len(pemesanan) > 0:
                        edit_pesanan = int(
                            input("Masukkan nomor pesanan yang ingin diedit: ")
                        )

                        nomor_pesanan = cari_nama(pemesanan, edit_pesanan)

                        if nomor_pesanan != "":
                            nama_game = pemesanan[nomor_pesanan]["nama"]

                            print("Nama game:", nama_game)
                            print("Harga lama:", pemesanan[nomor_pesanan]["harga"])
                            print("Jumlah lama:", pemesanan[nomor_pesanan]["jumlah"])

                            if nama_game in game:
                                stok_lama = pemesanan[nomor_pesanan]["jumlah"]
                                harga_baru = int(input("Masukkan harga baru: "))
                                jumlah_baru = int(input("Masukkan jumlah baru: "))

                                game[nama_game]["stok"] += stok_lama

                                if (
                                    harga_baru >= 0
                                    and jumlah_baru > 0
                                    and jumlah_baru <= game[nama_game]["stok"]
                                ):
                                    game[nama_game]["stok"] -= jumlah_baru

                                    pemesanan[nomor_pesanan]["harga"] = harga_baru
                                    pemesanan[nomor_pesanan]["jumlah"] = jumlah_baru
                                    pemesanan[nomor_pesanan]["subtotal"] = hitung_subtotal(harga_baru, jumlah_baru)

                                    print("Pesanan berhasil diedit")
                                    print("Sisa stok:", game[nama_game]["stok"])
                                else:
                                    game[nama_game]["stok"] -= stok_lama

                                    print("Harga atau jumlah tidak valid")
                                    print("Pesanan tidak diubah")
                            else:
                                print("Game tidak ditemukan")
                        else:
                            print("Nomor pesanan tidak valid")
                    else:
                        print("Belum ada pesanan")

                elif input_menu == 3:
                    if len(pemesanan) > 0:
                        hapus_pesanan = int(
                            input("Masukkan nomor pesanan yang ingin dihapus: ")
                        )

                        nomor_pesanan = cari_nama(pemesanan, hapus_pesanan)

                        if nomor_pesanan != "":
                            nama_game = pemesanan[nomor_pesanan]["nama"]

                            if nama_game in game:
                                game[nama_game]["stok"] += pemesanan[nomor_pesanan]["jumlah"]

                            del pemesanan[nomor_pesanan]
                            print("Pesanan berhasil dihapus")
                        else:
                            print("Nomor pesanan tidak valid")
                    else:
                        print("Belum ada pesanan")

                elif input_menu == 4:
                    for nomor in pemesanan:
                        nama_game = pemesanan[nomor]["nama"]
                        if nama_game in game:
                            game[nama_game]["stok"] += pemesanan[nomor]["jumlah"]
                    pemesanan = {}
                    print("Seluruh pesanan berhasil dihapus")
                elif input_menu == 5:
                    if len(pemesanan) > 0:
                        cetak_struk()
                    else:
                        print("Belum ada pesanan")
                elif input_menu == 6:
                    logout = True
                    os.system("cls")
                    print("Logout berhasil")
                elif input_menu == 7:
                    program_status = False
                    os.system("cls")
                    print("Program selesai. Terima kasih!")
                else:
                    print("Menu tidak valid")
            except ValueError:
                print("Input yang anda masukkan bukan Integer (angka)")