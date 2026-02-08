from prod_controll import class_new_product

class elektronik(class_new_product):
    def change_quantity(self, qty):
        self.quantity = qty
        print(f"Jumlah elektronik '{self.name}' diubah menjadi {self.quantity}.")

    def change_price(self, prc):
        self.price = prc
        print(f"Harga elektronik '{self.name}' diubah menjadi {self.price}.")

    def change_name(self, nm):
        self.name = nm
        print(f"Nama elektronik diubah menjadi '{self.name}'.")