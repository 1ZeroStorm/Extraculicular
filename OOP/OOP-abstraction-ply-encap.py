from abc import ABC, abstractmethod

# === Abstraction ===
class Character(ABC):
    def __init__(self, name, health):
        # === Encapsulation ===
        self.__health = health   # private attribute
        self.name = name

    def get_health(self):
        return self.__health

    def set_health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self, damage):
        pass


# === Polymorphism ===
class Warrior(Character):
    def attack(self):
        print(f"{self.name} swings a mighty sword!")
        return 15

    def defend(self, damage):
        reduced = damage - 5
        self.set_health(self.get_health() - reduced)
        print(f"{self.name} blocks with shield, health now {self.get_health()}")


class Mage(Character):
    def attack(self):
        print(f"{self.name} casts a fireball!")
        return 20

    def defend(self, damage):
        reduced = damage - 2
        self.set_health(self.get_health() - reduced)
        print(f"{self.name} uses magic barrier, health now {self.get_health()}")


class Archer(Character):
    def attack(self):
        print(f"{self.name} shoots an arrow!")
        return 10

    def defend(self, damage):
        self.set_health(self.get_health() - damage)
        print(f"{self.name} dodges but still takes damage, health now {self.get_health()}")


# === Game Simulation ===
def battle(c1, c2):
    print(f"\nBattle: {c1.name} vs {c2.name}")
    while c1.get_health() > 0 and c2.get_health() > 0:
        
         
        dmg1 = c1.attack() # c1 attacks c2
        c2.defend(dmg1) # c2 defends against damage from c1

        
        if c2.get_health() <= 0:
            print(f"{c2.name} has fallen! {c1.name} wins!")
            break
        

        dmg2 = c2.attack() # c2 attacks c1
        c1.defend(dmg2) # c1 defends against damage from c2

        if c1.get_health() <= 0:
            print(f"{c1.name} has fallen! {c2.name} wins!")
            break


# === Example Run ===
warrior = Warrior("Thorin", 100)
mage = Mage("Gandalf", 80)
archer = Archer("Legolas", 90)


battle(warrior, mage)
battle(mage, archer)
