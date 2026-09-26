nama = input("masukkan nama Anda: ")
nim = input("masukkan NIM Anda: ")

if nama == "johann" and nim == "27":
    pertalite = 10000
    pertamax = 12500
    pertamax_turbo = 15000
    bbm = int(input("masukkan jenis BBM yang ingin dibeli dalam angka (1 untuk pertalite/2 untuk pertamax/3 untuk pertamax turbo): "))
    liter = int(input("masukkan jumlah liter yang ingin dibeli: "))

    if bbm == 1:
        total_harga = pertalite * liter
    elif bbm == 2:
        total_harga = pertamax * liter
    elif bbm == 3:
        total_harga = pertamax_turbo * liter
    else:
        total_harga = False 

    if liter >= 10:
        diskon = total_harga * 0.1
    elif liter >= 5:
        diskon = total_harga * 0.05
    else:   
        diskon = 0

    if total_harga != False and liter > 0:
        member = input("apakah anda member (iya/tidak): ")
        if member == "iya":
            total_bayar = total_harga - diskon
            diskon_member = total_harga * 0.02
            total_bayar = total_bayar - diskon_member
        else:
            total_bayar = total_harga - diskon
        print()
        print("========== STRUK BENSIN ==========")
        print("| nama                  |", nama)
        print("| nim                   |", nim)
        print("| jenis BBM             |", bbm)
        print("| jumlah liter          |", liter)
        print("| total harga           |", total_harga)
        print("| diskon                |", diskon)
        print("| diskon member         |", diskon_member if member == "iya" else 0)
        print("----------------------------------")
        print("| total yang harus dibayar:", total_bayar)
        print("========== TERIMA KASIH ==========")    
    else:
        print("jenis BBM salah atau jumlah liter tidak valid")
else:
    print("nama atau nim salah")  