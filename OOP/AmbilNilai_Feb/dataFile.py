from management import class_management
from transactions import class_transaction
from discount import class_discount
import productfiles.createAlatTulis as createAlatTulis


class data:
    def __init__(self):
        self.data = [createAlatTulis.alat_tulis("pulpen", "5000", "10"),
                     createAlatTulis.alat_tulis("pensil", "3000", "15")]
        self.new_mana = class_management()
        self.new_trans = class_transaction()
        self.new_dis = class_discount()

    def get_management(self):
        ip_man = input("masukkan pilihan (1/2/3/4): ")
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
        self.data = self.new_trans.add_new_transaction(self.data, self.new_mana)

    def get_discount(self):
        self.data = self.new_dis.discount(self.data, self.new_mana)