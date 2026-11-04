"""Titik masuk program. Jalankan file ini: python main.py"""
from autentikasi import proses_login
from menu import menu_admin, menu_petugas


def main():
    program_status = True

    while program_status:
        hasil_login = proses_login()

        if hasil_login is None:
            print("\nKesempatan login habis")
            print("Program dihentikan")
            break

        nama, role = hasil_login

        if role == "admin":
            status = menu_admin()
        else:
            status = menu_petugas()

        if status == "keluar":
            program_status = False


if __name__ == "__main__":
    main()
