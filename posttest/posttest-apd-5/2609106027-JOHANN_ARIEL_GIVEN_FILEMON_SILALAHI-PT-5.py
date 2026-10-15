
import os

user = [
    ["admin", "admin123", "admin"],
    ["johann", "johann123", "petugas"]
]

game = [
    ["God Of War", "Action", 500000, 3],
    ["FIFA 23", "Sport", 400000, 5],
    ["GTA V", "Action", 300000, 2],
    ["The Sims 4", "Simulation", 200000, 4],
    ["Minecraft", "Adventure", 250000, 6]
]

pemesanan = []
program_status = True

while program_status == True:
    login_count = 3
    login_berhasil = False

    while login_count > 0 and login_berhasil == False:
        print("\n========== LOGIN ==========")
        nama = input("Masukkan nama user: ")
        password = input("Masukkan password user: ")

        login_count -= 1
        role = ""

        for i in range(len(user)):
            if nama == user[i][0] and password == user[i][1]:
                login_berhasil = True
                role = user[i][2]
                break

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
            print("\nDAFTAR GAME")
            print("No | Nama game | Genre | Harga | Stok")

            for i in range(len(game)):
                print(
                    i + 1, "|",
                    game[i][0], "|",
                    game[i][1], "|",
                    "Rp.", game[i][2], "|",
                    game[i][3]
                )

            print("\nDAFTAR USER")
            print("No | Nama user | Password | Role")

            for i in range(len(user)):
                print(
                    i + 1, "|",
                    user[i][0], "|",
                    user[i][1], "|",
                    user[i][2]
                )

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

            input_menu = int(input("Masukkan menu yang dipilih: "))

            if input_menu == 1:
                nama_game = input("Masukkan nama game: ")
                genre_game = input("Masukkan genre game: ")
                harga_game = int(input("Masukkan harga game: "))
                stok_game = int(input("Masukkan stok game: "))

                game.append([
                    nama_game, genre_game, harga_game, stok_game
                ])

                print("Game berhasil ditambahkan")

            elif input_menu == 2:
                edit_game = int(
                    input("Masukkan nomor game yang ingin diedit: ")
                )

                if edit_game > 0 and edit_game <= len(game):
                    nama_game = input("Masukkan nama game baru: ")
                    genre_game = input("Masukkan genre game baru: ")
                    harga_game = int(input("Masukkan harga game baru: "))
                    stok_game = int(input("Masukkan stok game baru: "))

                    stok_dipesan = 0

                    for i in range(len(pemesanan)):
                        if pemesanan[i][0] == game[edit_game - 1][0]:
                            stok_dipesan += pemesanan[i][3]

                    if stok_game >= stok_dipesan:
                        game[edit_game - 1] = [
                            nama_game,
                            genre_game,
                            harga_game,
                            stok_game - stok_dipesan
                        ]

                        for i in range(len(pemesanan)):
                            if pemesanan[i][0] == game[edit_game - 1][0]:
                                pemesanan[i][1] = genre_game

                        print("Game berhasil diedit")
                    else:
                        print("Stok tidak boleh lebih kecil dari jumlah yang dipesan")
                else:
                    print("Nomor game tidak valid")

            elif input_menu == 3:
                hapus_game = int(
                    input("Masukkan nomor game yang ingin dihapus: ")
                )

                if hapus_game > 0 and hapus_game <= len(game):
                    game_dihapus = game[hapus_game - 1][0]
                    ada_pesanan = False

                    for i in range(len(pemesanan)):
                        if pemesanan[i][0] == game_dihapus:
                            ada_pesanan = True

                    if ada_pesanan == False:
                        game.pop(hapus_game - 1)
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
                    user.append([
                        nama_user, password_user, role_user
                    ])
                    print("User berhasil ditambahkan")
                else:
                    print("Role tidak valid")

            elif input_menu == 5:
                edit_user = int(
                    input("Masukkan nomor user yang ingin diedit: ")
                )

                if edit_user > 0 and edit_user <= len(user):
                    nama_user = input("Masukkan nama user baru: ")
                    password_user = input("Masukkan password user baru: ")
                    role_user = input("Masukkan role user baru (admin/petugas): ")

                    if role_user == "admin" or role_user == "petugas":
                        user[edit_user - 1] = [
                            nama_user, password_user, role_user
                        ]
                        print("User berhasil diedit")
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

    elif role == "petugas":
        while program_status == True and logout == False:
            print("\nDAFTAR GAME")
            print("No | Nama game | Genre | Harga | Stok")

            for i in range(len(game)):
                print(
                    i + 1, "|",
                    game[i][0], "|",
                    game[i][1], "|",
                    "Rp.", game[i][2], "|",
                    game[i][3]
                )

            print("\nDAFTAR PESANAN")
            print("No | Nama game | Genre | Harga | Jumlah | Subtotal")

            for i in range(len(pemesanan)):
                print(
                    i + 1, "|",
                    pemesanan[i][0], "|",
                    pemesanan[i][1], "|",
                    "Rp.", pemesanan[i][2], "|",
                    pemesanan[i][3], "|",
                    "Rp.", pemesanan[i][4]
                )

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

            input_menu = int(input("Masukkan menu yang dipilih: "))

            if input_menu == 1:
                pesanan_baru = int(
                    input("Pilih nomor game yang ingin dipesan: ")
                )

                if pesanan_baru > 0 and pesanan_baru <= len(game):
                    indeks_game = pesanan_baru - 1
                    jumlah = int(
                        input("Masukkan jumlah game yang ingin dipesan: ")
                    )

                    if jumlah > 0 and jumlah <= game[indeks_game][3]:
                        nama_game = game[indeks_game][0]
                        genre_game = game[indeks_game][1]
                        harga_game = game[indeks_game][2]
                        subtotal = harga_game * jumlah

                        game[indeks_game][3] -= jumlah

                        pemesanan.append([
                            nama_game,
                            genre_game,
                            harga_game,
                            jumlah,
                            subtotal
                        ])

                        print("Pesanan berhasil ditambahkan")
                        print("Sisa stok:", game[indeks_game][3])
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

                    if edit_pesanan > 0 and edit_pesanan <= len(pemesanan):
                        indeks_pesanan = edit_pesanan - 1

                        print("Nama game:", pemesanan[indeks_pesanan][0])
                        print("Harga lama:", pemesanan[indeks_pesanan][2])
                        print("Jumlah lama:", pemesanan[indeks_pesanan][3])

                        indeks_game = -1

                        for i in range(len(game)):
                            if game[i][0] == pemesanan[indeks_pesanan][0]:
                                indeks_game = i
                                break

                        if indeks_game != -1:
                            stok_lama = pemesanan[indeks_pesanan][3]
                            game[indeks_game][3] += stok_lama
                            harga_baru = int(input("Masukkan harga baru: "))
                            jumlah_baru = int(input("Masukkan jumlah baru: "))

                            if (
                                harga_baru >= 0
                                and jumlah_baru > 0
                                and jumlah_baru <= game[indeks_game][3]
                            ):
                                game[indeks_game][3] -= jumlah_baru

                                pemesanan[indeks_pesanan][2] = harga_baru
                                pemesanan[indeks_pesanan][3] = jumlah_baru
                                pemesanan[indeks_pesanan][4] = harga_baru * jumlah_baru

                                print("Pesanan berhasil diedit")
                                print("Sisa stok:", game[indeks_game][3])
                            else:
                                game[indeks_game][3] -= stok_lama

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

                    if hapus_pesanan > 0 and hapus_pesanan <= len(pemesanan):
                        indeks_pesanan = hapus_pesanan - 1

                        for i in range(len(game)):
                            if game[i][0] == pemesanan[indeks_pesanan][0]:
                                game[i][3] += pemesanan[indeks_pesanan][3]
                                break

                        pemesanan.pop(indeks_pesanan)
                        print("Pesanan berhasil dihapus")
                    else:
                        print("Nomor pesanan tidak valid")
                else:
                    print("Belum ada pesanan")

            elif input_menu == 4:
                for i in range(len(pemesanan)):
                    for j in range(len(game)):
                        if game[j][0] == pemesanan[i][0]:
                            game[j][3] += pemesanan[i][3]
                            break

                pemesanan = []
                print("Seluruh pesanan berhasil dihapus")

            elif input_menu == 5:
                if len(pemesanan) > 0:
                    total_harga = 0

                    print("\n========== STRUK PEMBELIAN ==========")

                    for i in range(len(pemesanan)):
                        print("Nama game:", pemesanan[i][0])
                        print("Harga: Rp.", pemesanan[i][2])
                        print("Jumlah:", pemesanan[i][3])
                        print("Subtotal: Rp.", pemesanan[i][4])
                        print("-------------------------------------")

                        total_harga += pemesanan[i][4]

                    print("Total harga: Rp.", total_harga)
                    print("=====================================")
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
