from prod_controll import class_new_product

class buku(class_new_product):
    def change_quantity(self, qty):
        self.quantity = qty
        print(f"Jumlah buku '{self.name}' diubah menjadi {self.quantity}.")

    def change_price(self, prc):
        self.price = prc
        print(f"Harga buku '{self.name}' diubah menjadi {self.price}.")
    def change_name(self, nm):
        self.name = nm
        print(f"Nama buku diubah menjadi '{self.name}'.")