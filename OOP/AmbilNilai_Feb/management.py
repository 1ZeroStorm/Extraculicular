import productfiles.createAlatTulis as createAlatTulis
import productfiles.createBuku as createBuku
import productfiles.createElektronik as createElektronik


class class_management:
    def add(self, passed_data):

        print("=======================================================")
        print("Tipe Produk yang tersedia: alat_tulis, buku, elektronik")
        print("=======================================================")

        
        prod = None
        while True:
            type_product = input("Masukkan tipe produk (1/2/3): ").strip().lower()
            
            if type_product == "alat_tulis" or type_product == "1":
                prod = createAlatTulis.alat_tulis("", 0, 0)
                break
            elif type_product == "buku" or type_product == "2":
                prod = createBuku.buku("", 0, 0)
                break
            elif type_product == "elektronik" or type_product == "3":
                prod = createElektronik.elektronik("", 0, 0)
                break
            else:
                print("masukkan tipe produk yang valid")
        
        while True:
            try:  
                name = input("Masukkan nama produk: ")
                price = float(input("Masukkan harga produk: "))
                quantity = int(input("Masukkan jumlah produk: "))
                break
            except ValueError:
                print("Input tidak valid.")
        prod.name = name
        prod.price = price
        prod.quantity = quantity
            
        passed_data.append(prod)
        print(f"Produk '{name}' dengan harga {price} dan jumlah {quantity} telah ditambahkan.")
        return passed_data

    def read(self, passed_data):
        if not passed_data:
            print("Tidak ada produk tersedia.")
            return passed_data

        print("=======================================================")
        print("Daftar Produk:")
        for object in passed_data:
            print(f"Nama: {object.name}, Harga: {object.price}, Jumlah: {object.quantity}")
        print("=======================================================")

        return passed_data

    def update(self, passed_data):
        self.read(passed_data)
        
        while True: 
            try:
                name = input("Masukkan nama produk yang ingin diupdate: ")
                for obj in passed_data:
                    if obj.name == name:
                        print(f"Produk '{name}' ditemukan.")

                        new_price = input("Masukkan harga baru: ")
                        new_quantity = input("Masukkan jumlah baru: ")
                        new_name = input("Masukkan nama baru: ")

                        obj.change_price(new_price)
                        obj.change_quantity(new_quantity)
                        obj.change_name(new_name)
                        
                return passed_data
            except ValueError:
                print("Input tidak valid.")   
                
        

    def delete(self, passed_data):
        self.read(passed_data)
        name = input("Masukkan nama produk yang ingin dihapus: ")
        for obj in passed_data:
            if obj.name == name:
                passed_data.remove(obj)
                print(f"Produk '{name}' telah dihapus.")
                return passed_data
        
        if name not in [obj.name for obj in passed_data]:
            print(f"Produk '{name}' tidak ditemukan.")
            print(f"Produk '{name}' tidak ditemukan.")

        return passed_data
