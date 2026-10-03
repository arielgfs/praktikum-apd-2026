nama = "johann"
nim = "027"
parameter = 0
siswa = ["", "", "", "", "", "", "", "", "", ""]
kelas = ["", "", "", "", "", "", "", "", ""]
status_ujian = ["", "", "", "", "", "", "", "", ""]
nilai = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
kategori = ["", "", "", "", "", "", "", "", "", ""]
status_login = 0

username = input("masukkan username: ")
password = input("masukkan password: ")

while status_login < 3:
    if username == nama and password == nim:
        print("login berhasil")
        print()

        while True:
            siswa[parameter] = input("masukkan nama siswa: ")
            kelas[parameter] = input("masukkan kelas siswa: ")
            status_ujian[parameter] = input("apakah siswa tersebut mengikuti ujian? (ya/tidak): ")

            if status_ujian[parameter] == "ya":
                soal_benar = int(input("dari 20 soal, masukkan jumlah soal benar: "))

                soal_salah = int(input(
                    "dari 20 soal, masukkan jumlah soal salah: "))

                nilai[parameter] = soal_benar * 5

                if nilai[parameter] >= 80:
                    kategori[parameter] = "sangat baik"
                elif nilai[parameter] >= 60:
                    kategori[parameter] = "baik"
                elif nilai[parameter] >= 40:
                    kategori[parameter] = "cukup"
                else:
                    kategori[parameter] = "perlu belajar lagi"

            else:
                nilai[parameter] = 0
                kategori[parameter] = "perlu belajar lagi"

            parameter += 1

            pertanyaan = input(
                "apakah anda ingin menambahkan data siswa lagi? (ya/tidak): "
            )

            if pertanyaan == "tidak":
                break

            print()

        print()
        print("hasil data siswa")
        print()

        for kelas_sekarang in ["A", "B", "C"]:
            print("kelas", kelas_sekarang)

            for i in range(parameter):
                if kelas[i] == kelas_sekarang:
                    print("nama siswa:", siswa[i])
                    print("kelas siswa:", kelas[i])
                    print("status ujian:", status_ujian[i])
                    print("nilai siswa:", nilai[i])
                    print("kategori nilai:", kategori[i])
                    print()

        break

    else:
        print("login gagal")
        status_login += 1

        if status_login < 3:
            username = input("masukkan username: ")
            password = input("masukkan password: ")
        else:
            print("kesempatan login habis")