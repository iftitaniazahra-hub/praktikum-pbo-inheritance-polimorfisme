#Tugas 3 - Sistem Rekening Bank

def rp(angka):
    return "Rp" + f"{angka:,.0f}".replace(",", ".")

class RekeningBank:
    jenis = 'Umum'

    def __init__(self, nomor_rekening, nama_pemilik, saldo=0):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        if jumlah <= 0:
            print("Gagal! Jumlah setoran harus lebih dari 0")
            return False
        self.saldo += jumlah
        print(f"Setoran : {rp(jumlah)}")
        print("Berhasil!")
        print(f"Saldo akhir : {rp(self.saldo)}")
        return True
    def tarik(self, jumlah):
        print(f"Penarikan: {rp(jumlah)}")
        if jumlah <= 0:
            print(f"Gagal! Jumlah penarikna harus lebih dari 0")
            return False
        if jumlah > self.saldo:
            print ("Gagal! Saldo tidak mencukupi")
            return False
        self.saldo -= jumlah
        print("Berhasil")
        print(f"Saldo akhir: {rp(self.saldo)}")
        return True

    def info_rekening(self):
        print(f"No. Rek : {self.nomor_rekening}")
        print(f"Pemilik : {self.nama_pemilik}")
        print(f"Jenis : {self.jenis}")
        print(f"Saldo : {rp(self.saldo)}")

class RekeningTabungan(RekeningBank):
    jenis = "Tabungan"
    SALDO_MINIMAL = 50_000
 
    def __init__(self, nomor_rekening, nama_pemilik, saldo=0):
        super().__init__(nomor_rekening, nama_pemilik, saldo)
 
    def tarik(self, jumlah):
        print(f"Penarikan: {rp(jumlah)}")
        if jumlah <= 0:
            print("Gagal! Jumlah penarikan harus lebih dari 0.")
            return False
        if self.saldo - jumlah < self.SALDO_MINIMAL:
            print(f"Gagal! Saldo minimal {rp(self.SALDO_MINIMAL)} harus tersisa.")
            return False
        self.saldo -= jumlah
        print("Berhasil!")
        print(f"Saldo akhir: {rp(self.saldo)}")
        return True
 
 
class RekeningBisnis(RekeningBank):
    jenis = "Bisnis"
    BIAYA_ADMIN = 5_000
 
    def __init__(self, nomor_rekening, nama_pemilik, saldo=0):
        super().__init__(nomor_rekening, nama_pemilik, saldo)
 
    def tarik(self, jumlah):
        print(f"Penarikan: {rp(jumlah)}")
        if jumlah <= 0:
            print("Gagal! Jumlah penarikan harus lebih dari 0.")
            return False
        total = jumlah + self.BIAYA_ADMIN
        print(f"Biaya admin: {rp(self.BIAYA_ADMIN)}")
        if total > self.saldo:
            print("Gagal! Saldo tidak mencukupi (termasuk biaya admin).")
            return False
        self.saldo -= total
        print("Berhasil!")
        print(f"Saldo akhir: {rp(self.saldo)}")
        return True
 
 
if __name__ == "__main__":
    transaksi = [
        (RekeningTabungan("TAB-001", "Andi", 500_000), 200_000),
        (RekeningTabungan("TAB-002", "Sari", 120_000), 100_000),
        (RekeningBisnis("BIS-001", "Budi", 1_000_000), 200_000),
        (RekeningBisnis("BIS-002", "Rina", 150_000), 148_000),
    ]
 
    print("=== SISTEM REKENING BANK ===")
    for rekening, jumlah in transaksi:
        print(f"Pemilik : {rekening.nama_pemilik}")
        print(f"Jenis   : {rekening.jenis}")
        print(f"Saldo   : {rp(rekening.saldo)}")
        rekening.tarik(jumlah)
        print()
 
    print("--- Contoh setor & info rekening ---")
    r = RekeningTabungan("TAB-003", "Dewi", 100_000)
    r.setor(250_000)
    r.info_rekening()
        