class AkunBank:
    def __init__(self, saldo):
        self.__saldo = max(saldo, 0)
    
    def lihat_saldo(self):
        return self.__saldo
    
    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil menambah saldo sebesar {jumlah}")
        else:
            print("Jumlah tambahan harus lebih dari 0")
    
    def __internal_kurangi_saldo(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penarikan harus lebih dari 0")
            return False
        if jumlah > self.__saldo:
            print("Saldo tidak mencukupi")
            return False
        self.__saldo -= jumlah
        return True
    
    def tarik_saldo(self, jumlah):
        if self.__internal_kurangi_saldo(jumlah):
            print(f"Berhasil menarik saldo sebesar {jumlah}")
        else:
            print("Penarikan gagal")


# Main Program
def main():
    # 1. Minta user memasukkan saldo awal
    try:
        saldo_awal = float(input("Masukkan saldo awal: "))
    except ValueError:
        print("Input tidak valid, saldo diatur ke 0.")
        saldo_awal = 0
    
    # Buat objek AkunBank
    akun = AkunBank(saldo_awal)
    
    # 2. Tampilkan menu berulang menggunakan while True
    while True:
        print("\n=== MENU AKUN BANK ===")
        print("1. Lihat Saldo")
        print("2. Tambah Saldo")
        print("3. Tarik Saldo")
        print("4. Keluar")
        
        # Minta input pilihan menu
        try:
            pilihan = int(input("\nPilih menu (1-4): "))
        except ValueError:
            print("Input tidak valid! Harap masukkan angka 1-4.")
            continue
        
        # 3. Program berjalan sampai user memilih Keluar
        # 4. Tangani input menu yang tidak valid
        if pilihan == 1:
            print(f"\nSaldo saat ini: {akun.lihat_saldo():,.2f}")
        elif pilihan == 2:
            try:
                jumlah = float(input("Masukkan jumlah yang ingin ditambahkan: "))
                akun.tambah_saldo(jumlah)
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
        elif pilihan == 3:
            try:
                jumlah = float(input("Masukkan jumlah yang ingin ditarik: "))
                akun.tarik_saldo(jumlah)
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
        elif pilihan == 4:
            print("Terima kasih telah menggunakan layanan kami!")
            break
        else:
            print("Menu tidak valid! Harap pilih 1-4.")


if __name__ == "__main__":
    main()