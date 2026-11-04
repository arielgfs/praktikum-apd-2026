"""Penyimpanan data program (user, game, pemesanan) dan fungsi bantu data."""

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

# Dibungkus dictionary supaya nilainya bisa diubah dari file lain
counter = {"nomor_pesanan_baru": 1}


def cari_nama(kumpulan, nomor):
    """Mengambil key dari dictionary berdasarkan nomor urut (mulai dari 1)."""
    hasil = ""
    i = 1

    for nama_item in kumpulan:
        if i == nomor:
            hasil = nama_item
        i += 1

    return hasil


def hitung_subtotal(harga, jumlah):
    return harga * jumlah


def hitung_total_harga():
    total = 0
    for nomor in pemesanan:
        total += pemesanan[nomor]["subtotal"]
    return total
