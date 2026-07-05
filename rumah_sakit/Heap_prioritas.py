class BinaryHeap:
    def __init__(self):
        self.data = []

    def _priority(self, pasien):
        prioritas = {
            "Gawat Darurat": 3,
            "Mendesak": 2,
            "Non-Mendesak": 1
        }
        return prioritas.get(pasien.prioritas, 0)

    def is_empty(self):
        return len(self.data) == 0

    def insert(self, pasien):
        self.data.append(pasien)
        self._heapify_up(len(self.data)-1)
        print(f"\n{pasien.nama} masuk ke antrian prioritas.")

    def _heapify_up(self, index):

        while index > 0:

            parent = (index-1)//2

            if self._priority(self.data[index]) > self._priority(self.data[parent]):
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def delete_root(self):

        if self.is_empty():
            print("\nHeap kosong.")
            return None

        if len(self.data)==1:
            return self.data.pop()

        root = self.data[0]

        self.data[0]=self.data.pop()

        self._heapify_down(0)

        return root

    def _heapify_down(self,index):

        size=len(self.data)

        while True:

            left=2*index+1
            right=2*index+2
            terbesar=index

            if left<size and self._priority(self.data[left])>self._priority(self.data[terbesar]):
                terbesar=left

            if right<size and self._priority(self.data[right])>self._priority(self.data[terbesar]):
                terbesar=right

            if terbesar!=index:

                self.data[index],self.data[terbesar]=self.data[terbesar],self.data[index]
                index=terbesar

            else:
                break

    def peek(self):

        if self.is_empty():
            print("\nHeap kosong.")
            return None

        return self.data[0]

    def display(self):

        if self.is_empty():
            print("\nAntrian prioritas kosong.")
            return

        print("\n====== ANTRIAN PRIORITAS ======")

        for i,p in enumerate(self.data,start=1):

            print(f"{i}. ID : {p.id_pasien}")
            print(f"   Nama      : {p.nama}")
            print(f"   Prioritas : {p.prioritas}")
            print(f"   Keluhan   : {p.keluhan}")
            print("-"*35)
