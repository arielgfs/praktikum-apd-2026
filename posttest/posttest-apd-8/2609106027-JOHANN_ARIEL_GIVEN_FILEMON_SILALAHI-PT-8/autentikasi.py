"""Proses login pengguna."""
import storage
from read import tampilkan_info_login

BATAS_LOGIN = 3


def proses_login():
    """Mengembalikan (nama, role) jika berhasil, atau None jika kesempatan habis."""
    login_count = BATAS_LOGIN

    while login_count > 0:
        print("\n========== LOGIN ==========")
        nama = input("Masukkan nama user: ")
        password = input("Masukkan password user: ")

        login_count -= 1

        if nama in storage.user and password == storage.user[nama]["password"]:
            role = storage.user[nama]["role"]
            tampilkan_info_login(nama, role)
            return nama, role

        print("Nama user atau password salah")
        if login_count > 0:
            print("Login tersisa:", login_count, "kali")

    return None
