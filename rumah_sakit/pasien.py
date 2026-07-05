class Pasien:
    def __init__(self, id_pasien, nama, umur, keluhan, prioritas):
        self.id_pasien = id_pasien
        self.nama = nama
        self.umur = umur
        self.keluhan = keluhan
        self.prioritas = prioritas

    def __str__(self):
        return (
            f"ID        : {self.id_pasien}\n"
            f"Nama      : {self.nama}\n"
            f"Umur      : {self.umur}\n"
            f"Keluhan   : {self.keluhan}\n"
            f"Prioritas : {self.prioritas}"
        )