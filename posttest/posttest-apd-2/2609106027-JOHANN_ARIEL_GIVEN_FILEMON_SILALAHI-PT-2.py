bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10
bagasi = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]

total_berat_akhir_kg = (bagasi[0] + bagasi[1] + bagasi[2] + bagasi[3] + bagasi[4] + bagasi[5])
biaya_kompensasi = total_berat_akhir_kg * 0.05
rata_rata = total_berat_akhir_kg / len(bagasi)
nim = 27
boolean = nim < rata_rata
total_berat_akhir_gram = total_berat_akhir_kg * 1000

print("isi variabel bagasi_1:", bagasi_1)
print("isi variabel bagasi_2:", bagasi_2)
print("isi variabel bagasi_3:", bagasi_3)
print("isi variabel bagasi_4:", bagasi_4)
print("isi variabel bagasi_5:", bagasi_5)
print("isi variabel bagasi_6:", bagasi_6)
print("isi list bagasi:", bagasi)
print("total berat akhir (kg):", total_berat_akhir_kg)
print("total berat akhir (gram):", total_berat_akhir_gram)
print("biaya kompensasi:", biaya_kompensasi)
print("rata-rata berat:", rata_rata)
print("isi variabel boolean:", boolean)
print("bagasi dari indeks 2 sampai 4:", bagasi[2:5])  