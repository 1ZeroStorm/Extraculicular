class class_discount:
    def discount(self, passed_data, new_mana):
        new_mana.read(passed_data)
        ip = input("masukkan nama produk yang ingin didiskon: ")
        dis = float(input("masukkan persentase diskon (tanpa %) (contoh: diskon 50% -> 50, harga: 60000 -> 60000-60000*50%): "))
        for obj in passed_data:
            if obj.name == ip:
                original_price = float(obj.price)
                discount_amount = (dis / 100) * original_price
                new_price = original_price - discount_amount
                obj.price = str(round(new_price, 2))
                print(f"Diskon sebesar {dis}% telah diterapkan pada produk '{ip}'. Harga baru: {obj.price}")
                return passed_data
        print(f"Produk '{ip}' tidak ditemukan.")
        return passed_data
        