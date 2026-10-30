# Tugas 2 - Sistem Pengelolaan Civitas Akademika

class orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalan(self):
        print(f"Nama : {self.nama}")
        print(f"Umur : {self.umur}")
        print("Saya adalah seorang manusia")

class Mahasiswa(orang):
    def __init__(self, nama, umur, nim, jurusan):
        super().__init__(nama, umur)
        self.nim = nim
        self.jurusan = jurusan

    def perkenalan(self):
        print(f"Nama : {self.nama}")
        print(f"Umur : {self.umur}")
        print(f"NIM : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print("Saya mahasiwa yang sedang belajar")

    def belajar(self):
        print(f"{self.nama} sedang belajar {self.jurusan}")

class Dosen(orang):
    def __init__(self, nama, umur,  nidn, mata_kuliah):
        super().__init__(nama, umur)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def perkenalan(self):
       print(f"Nama : {self.nama}")
       print(f"Umur : {self.umur}")
       print(f"NIDN : {self.nidn}")
       print(f"Mata Kuliah : {self.mata_kuliah}") 
       print(f"Saya dosen yang mengajar {self.mata_kuliah}")

    def mengajar(self):
        print(f"{self.nama} sedang mengajar {self.mata_kuliah}")

if __name__ == "__main__":
    civitas = [
        Mahasiswa("Andi", 20, "25010001", "Teknik Informatika"),
        Mahasiswa("Sari", 21, "25010002", "Sistem Informasi"),
        Mahasiswa("Dewi", 19, "25010003", "Teknik Informatika"),
        Dosen("Budi", 35, "23020001", "Pemrograman Dasar"),
        Dosen("Rina", 30, "23020002", "Basis Data"),
    ]

    print("=== SISTEM AKADEMIK ===")
    for orang in civitas:
        orang.perkenalan()
        print()

    print("--- aktivitas ---")
    for orang in civitas:
        if isinstance(orang, Mahasiswa):
            orang.belajar()
        elif isinstance(orang, Dosen):
            orang.mengajar()