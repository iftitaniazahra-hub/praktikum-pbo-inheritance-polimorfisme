# Tugas 1 - Sistem Informasi Kendaraan (Inheritance & Polimorfisme)

class kendaraan:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

    def info_kendaraan(self):
        print(f"Merk : {self.merk}")
        print(f"Tahun : {self.tahun}")
        print(f"Warna : {self.warna}")
        print(f"Jenis : {self.__class__.__name__}")

    def bergerak(self):
        print("Kendaraan bergerak")

class Mobil(kendaraan):
    def __init__(self, merk, tahun, warna):
        super().__init__(merk, tahun, warna)
    def bergerak(self):
        print("Mobil berjalan menggunakan 4 roda")

class Motor(kendaraan):
    def __init__(self, merk, tahun, warna):
        super().__init__(merk, tahun, warna)
    def bergerak(self):
            print("Motor berjalan menggunakan 2 roda")

class Bus(kendaraan):
    def __init__(self, merk, tahun, warna):
        super().__init__(merk, tahun, warna)
    def bergerak(self):
        print("Bus menampung banyak penumpang")

if __name__ == "__main__":
    daftar_kendaraan = [
        Mobil("Toyota", 2022, "Hitam"),
        Mobil("Suzuki", 2020, "Silver"),
        Motor("Honda", 2023, "Merah"),
        Motor("Yamaha", 2021, "Biru"),
        Bus("Hino", 2021, "Putih"),
        Bus("Mercedes-Benz", 2019, "Kuning"),
    ]

print("===SISTEM INFORMASI KENDARAAN===")
for kendaraan in daftar_kendaraan:
    kendaraan.info_kendaraan()
    kendaraan.bergerak()
    print()