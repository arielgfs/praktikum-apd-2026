"""DELETE: menghapus game, pesanan satuan, dan seluruh pesanan."""
import storage
from storage import cari_nama


def hapus_game():
    nomor = int(input("Masukkan nomor game yang ingin dihapus: "))
    nama_dihapus = cari_nama(storage.game, nomor)

    if nama_dihapus == "":
        print("Nomor game tidak valid")
        return

    ada_pesanan = False
    for no_pesanan in storage.pemesanan:
        if storage.pemesanan[no_pesanan]["nama"] == nama_dihapus:
            ada_pesanan = True

    if not ada_pesanan:
        del storage.game[nama_dihapus]
        print("Game berhasil dihapus")
    else:
        print("Game tidak bisa dihapus karena masih ada pesanan")


def hapus_pesanan():
    if len(storage.pemesanan) == 0:
        print("Belum ada pesanan")
        return

    nomor = int(input("Masukkan nomor pesanan yang ingin dihapus: "))
    nomor_pesanan = cari_nama(storage.pemesanan, nomor)

    if nomor_pesanan == "":
        print("Nomor pesanan tidak valid")
        return

    nama_game = storage.pemesanan[nomor_pesanan]["nama"]
    if nama_game in storage.game:
        storage.game[nama_game]["stok"] += storage.pemesanan[nomor_pesanan]["jumlah"]

    del storage.pemesanan[nomor_pesanan]
    print("Pesanan berhasil dihapus")


def hapus_semua_pesanan():
    for nomor in storage.pemesanan:
        nama_game = storage.pemesanan[nomor]["nama"]
        if nama_game in storage.game:
            storage.game[nama_game]["stok"] += storage.pemesanan[nomor]["jumlah"]

    storage.pemesanan.clear()
    print("Seluruh pesanan berhasil dihapus")
