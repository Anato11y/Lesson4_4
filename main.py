# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.

# Создание абстрактного класса Weapon
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Реализация конкретных типов оружия

class Sword(Weapon):
    def attack(self):
        return "удар мечом"

class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"

# Модификация класса Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.attack()}.")

    def attack(self, monster):
        if self.weapon:
            attack_result = self.weapon.attack()
            print(f"{self.name} наносит {attack_result}.")
            monster.take_damage()
        else:
            print(f"{self.name} пытается атаковать, но у него нет оружия!")

# Реализация класса Monster и механизма боя
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self):
        self.health -= 10
        if self.health <= 0:
            print(f"{self.name} побежден!")
        else:
            print(f"{self.name} получил урон, оставшееся здоровье: {self.health}")

# Создаем бойца и монстра
fighter = Fighter("Боец")
monster = Monster("Монстр", 20)

# Выбор и использование меча
sword = Sword()
fighter.change_weapon(sword)
fighter.attack(monster)

# Выбор и использование лука
bow = Bow()
fighter.change_weapon(bow)
fighter.attack(monster)
