from pasien import Pasien
from BST_pasien import BSTPasien
from Queue_pasien import QueuePasien
from Heap_prioritas import BinaryHeap
from Stack_riwayat import StackRiwayat


# ==============================
# Membuat Objek
# ==============================
bst = BSTPasien()
queue = QueuePasien()
heap = BinaryHeap()
riwayat = StackRiwayat()


# ==============================
# Tambah Pasien
# ==============================
def tambah_pasien():

    print("\n===== TAMBAH PASIEN =====")

    id_pasien = int(input("ID Pasien : "))

    # Cek apakah ID sudah ada
    if bst.search(id_pasien):
        print("\nID Pasien sudah digunakan!")
        return

    nama = input("Nama : ")
    umur = int(input("Umur : "))
    keluhan = input("Keluhan : ")

    print("\n===== PRIORITAS =====")
    print("1. Gawat Darurat")
    print("2. Mendesak")
    print("3. Non-Mendesak")

    pilihan = input("Pilih : ")

    if pilihan == "1":
        prioritas = "Gawat Darurat"

    elif pilihan == "2":
        prioritas = "Mendesak"

    else:
        prioritas = "Non-Mendesak"

    pasien = Pasien(
        id_pasien,
        nama,
        umur,
        keluhan,
        prioritas
    )

    # Masuk Queue
    queue.enqueue(pasien)

    # Masuk BST
    bst.insert(pasien)

    # Masuk Heap
    heap.insert(pasien)

    print("\nData pasien berhasil ditambahkan.")
    
# ==============================
# Cari Pasien
# ==============================
def cari_pasien():

    print("\n===== CARI PASIEN =====")

    id_pasien = int(input("Masukkan ID Pasien : "))

    pasien = bst.search(id_pasien)

    if pasien:

        print("\n===== DATA PASIEN =====")
        print(pasien)

    else:

        print("\nPasien tidak ditemukan.")
        
# ==============================
# Hapus Pasien
# ==============================
def hapus_pasien():

    print("\n===== HAPUS PASIEN =====")

    id_pasien = int(input("Masukkan ID Pasien : "))

    pasien = bst.search(id_pasien)

    if pasien is None:

        print("\nPasien tidak ditemukan.")
        return

    bst.delete(id_pasien)

    print("\nPasien berhasil dihapus dari BST.")
    
# ==============================
# Data Pasien BST
# ==============================
def tampil_data_pasien():

    bst.inorder()
    
# ==============================
# Queue
# ==============================
def tampil_queue():

    queue.display()


def peek_queue():

    pasien = queue.peek()

    if pasien:

        print("\n===== PASIEN TERDEPAN =====")
        print(pasien)
        
def remove_by_id(self, id_pasien):
    if self.is_empty():
        return None

    for i, pasien in enumerate(self.queue):
        if pasien.id_pasien == id_pasien:
            return self.queue.pop(i)

    return None

# ==============================
# Binary Heap
# ==============================
def tampil_heap():

    heap.display()


def peek_heap():

    pasien = heap.peek()

    if pasien:

        print("\n===== PRIORITAS TERTINGGI =====")
        print(pasien)
        
# ==============================
# Layani Pasien
# ==============================
def layani_pasien():

    print("\n===== LAYANI PASIEN =====")

    pasien = heap.delete_root()

    if pasien is None:
        return

    # Hapus dari Queue
    queue.remove_by_id(pasien.id_pasien)

    # Simpan ke Riwayat
    riwayat.push(pasien)

    print("\nPasien berhasil dilayani.")
    print(pasien)
    
# ==============================
# Riwayat Pemeriksaan
# ==============================
def tampil_riwayat():

    riwayat.display()


def peek_riwayat():

    pasien = riwayat.peek()

    if pasien:

        print("\n===== RIWAYAT TERAKHIR =====")
        print(pasien)
        
# ==============================
# Undo Riwayat
# ==============================
def undo_riwayat():

    pasien = riwayat.pop()

    if pasien is None:
        return

    print("\nRiwayat terakhir berhasil dihapus.")
    print(pasien)
    
# ==============================
# Statistik
# ==============================
def statistik():

    print("\n===== STATISTIK SISTEM =====")

    print(f"Jumlah Data BST      : {bst.node_count()}")
    print(f"Tinggi BST           : {bst.height()}")

    print(f"Jumlah Queue         : {queue.size()}")
    print(f"Jumlah Heap          : {heap.size()}")
    print(f"Jumlah Riwayat       : {riwayat.size()}")
    
# ==============================
# Menu Utama
# ==============================
while True:

    print("\n")
    print("=" * 50)
    print("      SISTEM MANAJEMEN RUMAH SAKIT")
    print("=" * 50)
    print("1. Tambah Pasien")
    print("2. Cari Pasien")
    print("3. Hapus Pasien")
    print("4. Tampilkan Data Pasien (BST)")
    print("-" * 50)
    print("5. Tampilkan Antrian (Queue)")
    print("6. Peek Antrian")
    print("-" * 50)
    print("7. Tampilkan Prioritas (Heap)")
    print("8. Peek Prioritas")
    print("-" * 50)
    print("9. Layani Pasien")
    print("-" * 50)
    print("10. Tampilkan Riwayat")
    print("11. Peek Riwayat")
    print("12. Undo Riwayat")
    print("-" * 50)
    print("13. Statistik")
    print("0. Keluar")
    print("=" * 50)

    menu = input("Pilih Menu : ")

    if menu == "1":
        tambah_pasien()

    elif menu == "2":
        cari_pasien()

    elif menu == "3":
        hapus_pasien()

    elif menu == "4":
        tampil_data_pasien()

    elif menu == "5":
        tampil_queue()

    elif menu == "6":
        peek_queue()

    elif menu == "7":
        tampil_heap()

    elif menu == "8":
        peek_heap()

    elif menu == "9":
        layani_pasien()

    elif menu == "10":
        tampil_riwayat()

    elif menu == "11":
        peek_riwayat()

    elif menu == "12":
        undo_riwayat()

    elif menu == "13":
        statistik()

    elif menu == "0":
        print("\nTerima kasih telah menggunakan Sistem Manajemen Rumah Sakit.")
        break

    else:
        print("\nMenu tidak tersedia.")