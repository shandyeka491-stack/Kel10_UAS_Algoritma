class StackRiwayat:
    def __init__(self):
        self.stack = []

    def push(self, pasien):
        self.stack.append(pasien)
        print(f"\nPasien {pasien.nama} telah masuk ke riwayat.")

    def pop(self):
        if self.is_empty():
            print("\nRiwayat pasien masih kosong.")
            return None

        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("\nRiwayat pasien masih kosong.")
            return None

        return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("\nBelum ada riwayat pasien.")
            return

        print("\n========== RIWAYAT PASIEN ==========")

        nomor = 1
        for pasien in reversed(self.stack):
            print(f"{nomor}. ID      : {pasien.id_pasien}")
            print(f"   Nama    : {pasien.nama}")
            print(f"   Umur    : {pasien.umur}")
            print(f"   Keluhan : {pasien.keluhan}")
            print("-" * 35)
            nomor += 1

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)