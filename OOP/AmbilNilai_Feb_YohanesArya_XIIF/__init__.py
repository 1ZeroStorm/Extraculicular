from dataFile import data

def main():
    new_data = data() 
    
    pilihan = """
    1) manage
    2) transaksi
    3) tambah diskon
    4) keluar
    """

    pilihan_managemen = """
        1) tambah produk
        2) lihat produk
        3) update produk
        4) hapus produk
    """

    while True:
        print(pilihan)
        ip = input("masukkan pilihan (1/2/3): ")
        
        if ip == "1":
            print(pilihan_managemen)
            new_data.get_management()
        elif ip == "2":
            print("transaksi")
            new_data.get_transaction()
        elif ip == "3":
            print("tambah diskon")
            new_data.get_discount()
        elif ip == "4":
            print("keluar program")
            break

if __name__ == "__main__":
    main()