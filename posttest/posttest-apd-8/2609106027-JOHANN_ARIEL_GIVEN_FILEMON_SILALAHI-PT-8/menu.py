import os
import inquirer
import storage
from read import (
    tampilkan_game, tampilkan_user, tampilkan_pesanan,
    tampilkan_menu, cetak_struk
)
from create import tambah_game, tambah_user, tambah_pesanan
from update import edit_game, edit_user, edit_pesanan
from delete import hapus_game, hapus_pesanan, hapus_semua_pesanan


def ambil_menu(daftar_menu):
    pertanyaan = [
        inquirer.List(
            "menu",
            message="Pilih menu",
            choices=daftar_menu
        )
    ]

    jawaban = inquirer.prompt(pertanyaan)

    return daftar_menu.index(jawaban["menu"]) + 1


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def menu_admin():
    daftar_menu = [
        "Tambah Game",
        "Edit Game",
        "Hapus Game",
        "Tambah User",
        "Edit User",
        "Logout",
        "Keluar dari Program"
    ]

    while True:
        tampilkan_game()
        tampilkan_user()
        tampilkan_menu("MENU ADMIN", daftar_menu)

        pilihan = ambil_menu(daftar_menu)

        if pilihan == 1:
            tambah_game()

        elif pilihan == 2:
            edit_game()

        elif pilihan == 3:
            hapus_game()

        elif pilihan == 4:
            tambah_user()

        elif pilihan == 5:
            edit_user()

        elif pilihan == 6:
            bersihkan_layar()
            print("Logout berhasil")
            return "logout"

        elif pilihan == 7:
            bersihkan_layar()
            print("Program selesai. Terima kasih!")
            return "keluar"


def menu_petugas():
    daftar_menu = [
        "Tambah Pesanan",
        "Edit Pesanan",
        "Hapus Pesanan Berdasarkan Nomor Pesanan",
        "Hapus Seluruh Pesanan",
        "Print Struk",
        "Logout",
        "Keluar dari Program"
    ]

    while True:
        tampilkan_game()
        tampilkan_pesanan()
        tampilkan_menu("MENU PETUGAS", daftar_menu)

        pilihan = ambil_menu(daftar_menu)

        if pilihan == 1:
            tambah_pesanan()

        elif pilihan == 2:
            edit_pesanan()

        elif pilihan == 3:
            hapus_pesanan()

        elif pilihan == 4:
            hapus_semua_pesanan()

        elif pilihan == 5:
            if len(storage.pemesanan) > 0:
                cetak_struk()
            else:
                print("Belum ada pesanan")

        elif pilihan == 6:
            bersihkan_layar()
            print("Logout berhasil")
            return "logout"

        elif pilihan == 7:
            bersihkan_layar()
            print("Program selesai. Terima kasih!")
            return "keluar"