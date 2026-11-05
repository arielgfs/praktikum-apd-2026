from prettytable import PrettyTable
import storage

def format_rupiah(angka):
    return "Rp. " + format(angka, ",").replace(",", ".")


def tampilkan_game():
    tabel = PrettyTable()
    tabel.title = "DAFTAR GAME"
    tabel.field_names = ["No", "Nama Game", "Genre", "Harga", "Stok"]
    tabel.align["Nama Game"] = "l"
    tabel.align["Genre"] = "l"
    tabel.align["Harga"] = "r"

    i = 1
    for nama_game in storage.game:
        tabel.add_row([
            i,
            nama_game,
            storage.game[nama_game]["genre"],
            format_rupiah(storage.game[nama_game]["harga"]),
            storage.game[nama_game]["stok"]
        ])
        i += 1

    print()
    print(tabel)


def tampilkan_user():
    tabel = PrettyTable()
    tabel.title = "DAFTAR USER"
    tabel.field_names = ["No", "Nama User", "Password", "Role"]
    tabel.align["Nama User"] = "l"
    tabel.align["Password"] = "l"

    i = 1
    for nama_user in storage.user:
        tabel.add_row([
            i,
            nama_user,
            storage.user[nama_user]["password"],
            storage.user[nama_user]["role"]
        ])
        i += 1

    print()
    print(tabel)


def tampilkan_pesanan():
    tabel = PrettyTable()
    tabel.title = "DAFTAR PESANAN"
    tabel.field_names = ["No", "Nama Game", "Genre", "Harga", "Jumlah", "Subtotal"]
    tabel.align["Nama Game"] = "l"
    tabel.align["Genre"] = "l"
    tabel.align["Harga"] = "r"
    tabel.align["Subtotal"] = "r"

    i = 1
    for nomor in storage.pemesanan:
        pesanan = storage.pemesanan[nomor]
        tabel.add_row([
            i,
            pesanan["nama"],
            pesanan["genre"],
            format_rupiah(pesanan["harga"]),
            pesanan["jumlah"],
            format_rupiah(pesanan["subtotal"])
        ])
        i += 1

    print()
    print(tabel)


def tampilkan_menu(judul, daftar_menu):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = ["No", "Menu"]
    tabel.align["Menu"] = "l"

    i = 1
    for item in daftar_menu:
        tabel.add_row([i, item])
        i += 1

    print()
    print(tabel)


def tampilkan_info_login(nama, role):
    tabel = PrettyTable()
    tabel.title = "LOGIN BERHASIL"
    tabel.header = False
    tabel.add_row(["Selamat datang", nama])
    tabel.add_row(["Role anda", role])
    tabel.align = "l"

    print()
    print(tabel)


def cetak_struk():
    tabel = PrettyTable()
    tabel.title = "STRUK PEMBELIAN"
    tabel.field_names = ["No", "Nama Game", "Harga", "Jumlah", "Subtotal"]
    tabel.align["Nama Game"] = "l"
    tabel.align["Harga"] = "r"
    tabel.align["Subtotal"] = "r"

    i = 1
    for nomor in storage.pemesanan:
        pesanan = storage.pemesanan[nomor]
        tabel.add_row([
            i,
            pesanan["nama"],
            format_rupiah(pesanan["harga"]),
            pesanan["jumlah"],
            format_rupiah(pesanan["subtotal"])
        ])
        i += 1

    tabel.add_divider()
    tabel.add_row([
        "", "TOTAL HARGA", "", "",
        format_rupiah(storage.hitung_total_harga())
    ])

    print()
    print(tabel)
