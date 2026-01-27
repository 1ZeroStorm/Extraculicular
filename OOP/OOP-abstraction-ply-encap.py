from abc import ABC, abstractmethod

# === Abstraction ===
class Character(ABC):
    def __init__(self, name, health):
        # === Encapsulation ===
        self.__health = health   # private attribute
        self.name = name

    def get_health(self):
        return self.__health

    def set_health(self, value): #reduce health 
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
        print(f"{self.name} swings a sword!")
        return 15

    def defend(self, damage):
        reduced = damage - 5
        self.set_health(self.get_health() - reduced)
        print(f"{self.name} blocks with sword but still takes damage, health now {self.get_health()}")


class Mage(Character):
    def attack(self):
        print(f"{self.name} casts a reverse curse technique: RED!")
        return 20

    def defend(self, damage):
        reduced = damage - 2
        self.set_health(self.get_health() - reduced)
        print(f"{self.name} uses infinite barrier, health now {self.get_health()}")

class Assassin(Character):
    def attack(self):
        print(f"{self.name} strikes with a hidden blade!")
        return 25

    def defend(self, damage):
        reduced = damage - 2
        self.set_health(self.get_health() - reduced)
        print(f"{self.name} dodges but still takes damage, health now {self.get_health()}")

class Archer(Character):
    def attack(self):
        print(f"{self.name} shoots a blazing arrow!")
        return 10

    def defend(self, damage):
        self.set_health(self.get_health() - damage)
        print(f"{self.name} gets hit but regenerates, health now {self.get_health()}")

class createGaldiatorArena:
    def __init__(self, *character):
        self.characters = list(character)

    def startwar(self):
        for chara in self.characters:
            for enemy in self.characters:
                if chara != enemy:
                    print(f"\nBattle: {chara.name} vs {enemy.name}")
                    while chara.get_health() > 0 and enemy.get_health() > 0:
                        dmg = chara.attack()
                        enemy.defend(dmg)
                        if enemy.get_health() <= 0:
                            print(f"{enemy.name} has fallen! {chara.name} wins!")
                            break

                        dmg = enemy.attack()
                        chara.defend(dmg)
                        if chara.get_health() <= 0:
                            print(f"{chara.name} has fallen! {enemy.name} wins!")
                            break
                    print("one or two character(s) has fallen, moving to next battle...")



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
warrior = Warrior("Guts (warrior)", 100)
mage = Mage("Gojo (mage)", 80)
archer = Archer("Sukuna (archer)", 90)
assassin = Assassin("Jinwoo (assassin)", 85)

#battle(warrior, mage)
#battle(mage, archer)
arena = createGaldiatorArena(warrior, mage, archer, assassin)
arena.startwar()
