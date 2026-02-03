import importlib.resources as pkg_resources
import newproduct.productfiles.createAlatTulis as createAlatTulis
import newproduct.productfiles.createBuku as createBuku
import newproduct.productfiles.createElektronik as createElektronik


class class_management:
    def add(self, passed_data):

        print("=======================================================")
        print("Tipe Produk yang tersedia: alat_tulis, buku, elektronik")
        print("=======================================================")
        
        type_product = input("Masukkan tipe produk: ").strip().lower()
        name = input("Masukkan nama produk: ")
        price = input("Masukkan harga produk: ")
        quantity = input("Masukkan jumlah produk: ")

        if type_product == "alat_tulis":
            prod = createAlatTulis.alat_tulis(name, price, quantity)
        elif type_product == "buku":
            prod = createBuku.buku(name, price, quantity)
        elif type_product == "elektronik":
            prod = createElektronik.elektronik(name, price, quantity)
        
        passed_data.append(prod)
        print(f"Produk '{name}' dengan harga {price} dan jumlah {quantity} telah ditambahkan.")
        return passed_data

    def read(self, passed_data):
        if not passed_data:
            print("Tidak ada produk tersedia.")
            return

        print("Daftar Produk:")
        for object in passed_data:
            print(f"Nama: {object.name}, Harga: {object.price}, Jumlah: {object.quantity}")

        return passed_data

    def update(self, passed_data):
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

        if name not in [obj.name for obj in passed_data]:
            print(f"Produk '{name}' tidak ditemukan.")
        else:
            print(f"Produk '{name}' telah diperbarui.")
        return passed_data

    def delete(self, passed_data):
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
