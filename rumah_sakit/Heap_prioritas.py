class BinaryHeap:
    def __init__(self):
        self.heap = []

    # ==========================
    # Menentukan nilai prioritas
    # ==========================
    def priority_value(self, pasien):
        prioritas = {
            "Gawat Darurat": 3,
            "Mendesak": 2,
            "Non-Mendesak": 1
        }
        return prioritas.get(pasien.prioritas, 0)

    # ==========================
    # Mengecek heap kosong
    # ==========================
    def is_empty(self):
        return len(self.heap) == 0

    # ==========================
    # Insert
    # ==========================
    def insert(self, pasien):
        self.heap.append(pasien)
        self.heapify_up(len(self.heap) - 1)
        print(f"\n{pasien.nama} berhasil masuk ke antrian prioritas.")

    # ==========================
    # Heapify Up
    # ==========================
    def heapify_up(self, index):

        while index > 0:

            parent = (index - 1) // 2

            if self.priority_value(self.heap[index]) > self.priority_value(self.heap[parent]):
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    # ==========================
    # Delete Root
    # ==========================
    def delete_root(self):

        if self.is_empty():
            print("\nAntrian prioritas kosong.")
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify_down(0)

        return root

    # ==========================
    # Heapify Down
    # ==========================
    def heapify_down(self, index):

        size = len(self.heap)

        while True:

            left = (2 * index) + 1
            right = (2 * index) + 2

            terbesar = index

            if (
                left < size
                and self.priority_value(self.heap[left])
                > self.priority_value(self.heap[terbesar])
            ):
                terbesar = left

            if (
                right < size
                and self.priority_value(self.heap[right])
                > self.priority_value(self.heap[terbesar])
            ):
                terbesar = right

            if terbesar != index:
                self.heap[index], self.heap[terbesar] = (
                    self.heap[terbesar],
                    self.heap[index],
                )
                index = terbesar
            else:
                break

    # ==========================
    # Peek
    # ==========================
    def peek(self):

        if self.is_empty():
            print("\nAntrian prioritas kosong.")
            return None

        return self.heap[0]

    # ==========================
    # Display
    # ==========================
    def display(self):

        if self.is_empty():
            print("\nAntrian prioritas kosong.")
            return

        print("\n======= ANTRIAN PRIORITAS =======")

        for i, pasien in enumerate(self.heap, start=1):

            print(f"{i}. ID        : {pasien.id_pasien}")
            print(f"   Nama      : {pasien.nama}")
            print(f"   Umur      : {pasien.umur}")
            print(f"   Keluhan   : {pasien.keluhan}")
            print(f"   Prioritas : {pasien.prioritas}")
            print("-" * 35)

    # ==========================
    # Size
    # ==========================
    def size(self):
        return len(self.heap)