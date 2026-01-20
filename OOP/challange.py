# Base class
class Character:
    def __init__(self, name, health, mp):
        self.name = name
        self.health = health
        self.mp = mp

    def attack(self, other):
        print(f'karakter menyerang {other.name}')

    def is_alive(self):
        return self.health > 0

# Derived class: Warrior
class Warrior(Character):
    def attack(self, other):
        damage = 10
        if other.health - damage >= 0:
            other.health -= damage
            print(f"{self.name} casts a fireball at {other.name} for {damage} damage!")
            
            self.mp -= 10
            print(f'Mp Warrior: {self.mp}')

            print(f'current enemy health ({other.name}): {other.health}')
        else:
            print(f"{self.name} casts a fireball at {other.name} for {other.health} damage!")
            other.health = 0


    def get_hp(self):
        return self.health

# Derived class: Mage
class Mage(Character):
    def attack(self, other):
        damage = 12

        if other.health - damage >= 0:
            other.health -= damage
            print(f"{self.name} casts a fireball at {other.name} for {damage} damage!")
            
            self.mp -= 10
            print(f'Mp Mage: {self.mp}')

            print(f'current enemy health ({other.name}): {other.health}')
        else:
            print(f"{self.name} casts a fireball at {other.name} for {other.health} damage!")
            other.health = 0
            
        

    def get_hp(self):
        return self.health
    
class Dragon:
    def __init__(self, name, hp):
        self.health = hp
        self.name = name
    def get_hp(self):
        print(f"dragon HP:{self.health}")
        
# Example gameplay
warrior = Warrior("Wili", 100, 500)
mage = Mage("Nala", 100, 500)
dragon = Dragon('Kaiser',300)

party = [mage, warrior]

def attack_in_party():
    while dragon.health > 0:
        for character in party:
            character.attack(dragon)
        dragon.get_hp()
        print("+++++++++++++++++++++++")

attack_in_party()


