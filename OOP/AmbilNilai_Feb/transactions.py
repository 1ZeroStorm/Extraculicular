class class_transaction:
    def add_new_transaction(self, passed_data, new_mana):
        new_mana.read(passed_data)
        ip = input("masukkan nama produk yang dibeli: ")
        for obj in passed_data:
            if obj.name == ip:
                jumlah_beli = int(input("masukkan jumlah produk yang dibeli: "))
                if jumlah_beli > int(obj.quantity):
                    print("Stok tidak mencukupi.")
                    return passed_data
                else:
                    total_harga = jumlah_beli * int(obj.price)
                    money = int(input("masukkan uang pembeli: "))
                    if money < total_harga:
                        print("Uang tidak cukup.")
                        return passed_data
                    kembalian = money - total_harga

                    obj.quantity = str(int(obj.quantity) - jumlah_beli)
                    print(f"Transaksi berhasil! Total harga: {total_harga}")
                    
                
                    struk = '''
                    ===================== STRUK PEMBELIAN =====================
                    Produk: {ip}
                    Jumlah: {jumlah_beli}
                    Total Harga: {total_harga}
                    Kembalian: {kembalian}
                    ===========================================================
                    '''
                    
                    print(struk.format(ip=ip, jumlah_beli=jumlah_beli, total_harga=total_harga, kembalian=kembalian))
                    return passed_data