from data.dataFile import data

def main():
    new_data = data() 

    pilihan = """
    1) manage
    2) transaksi
    3) tambah diskon
    """

    pilihan_managemen = """
        1) tambah produk
        2) lihat produk
        3) update produk
        4) hapus produk
    """

    ip = input("masukkan pilihan (1/2/3)")
    
    if ip == "1":
        print(pilihan_managemen)
        data.get_management()
    elif ip == "2":
        print("transaksi")
        data.get_transaction()
    elif ip == "3":
        print("tambah diskon")

if __name__ == "__main__":
    main()