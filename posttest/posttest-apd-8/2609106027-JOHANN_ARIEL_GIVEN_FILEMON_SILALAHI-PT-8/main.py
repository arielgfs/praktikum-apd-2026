import inquirer
from autentikasi import proses_login
from menu import menu_admin, menu_petugas, bersihkan_layar
from create import tambah_user


def menu_awal():
    daftar_menu = [
        "Login",
        "Registrasi Akun",
        "Keluar dari Program"
    ]

    pertanyaan = [
        inquirer.List(
            "menu",
            message="SELAMAT DATANG",
            choices=daftar_menu
        )
    ]

    jawaban = inquirer.prompt(pertanyaan)

    return daftar_menu.index(jawaban["menu"]) + 1


def main():
    program_status = True

    while program_status:
        pilihan = menu_awal()

        if pilihan == 1:
            hasil_login = proses_login()

            if hasil_login is None:
                print("\nKesempatan login habis")
                print("Silakan coba login kembali")
                continue

            nama, role = hasil_login

            if role == "admin":
                status = menu_admin()
            else:
                status = menu_petugas()

            if status == "keluar":
                program_status = False

        elif pilihan == 2:
            tambah_user()

        elif pilihan == 3:
            bersihkan_layar()
            print("Program selesai. Terima kasih!")
            return


if __name__ == "__main__":
    main()