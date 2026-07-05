class QueuePasien:
    def __init__(self):
        self.queue = []

    def enqueue(self, pasien):
        self.queue.append(pasien)
        print(f"\nPasien {pasien.nama} berhasil masuk ke antrian.")

    def dequeue(self):
        if self.is_empty():
            print("\nAntrian masih kosong.")
            return None

        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            print("\nAntrian masih kosong.")
            return None

        return self.queue[0]

    def display(self):
        if self.is_empty():
            print("\nAntrian pasien kosong.")
            return

        print("\n========== ANTRIAN PASIEN ==========")
        for i, pasien in enumerate(self.queue, start=1):
            print(
                f"{i}. "
                f"ID      : {pasien.id_pasien}\n"
                f"   Nama    : {pasien.nama}\n"
                f"   Umur    : {pasien.umur}\n"
                f"   Keluhan : {pasien.keluhan}\n"
            )

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
