from management.man_controll import class_management
from transaction.trans_controll import class_transaction


class data:
    def __init__(self):
        self.data = []
        self.new_mana = class_management()
        self.new_trans = class_transaction()

    def get_management(self):
        ip_man = input("masukkan pilihan (1/2/3/4)")
        if ip_man == "1":
            print("tambah produk")
            self.data = self.new_mana.add(self.data)
        elif ip_man == "2":
            print("lihat produk")
            self.data = self.new_mana.read(self.data)
        elif ip_man == "3":
            print("update produk")
            self.data = self.new_mana.update(self.data)
        elif ip_man == "4":
            print("hapus produk")
            self.data = self.new_mana.delete(self.data)
    
    def get_transaction(self):
        pass