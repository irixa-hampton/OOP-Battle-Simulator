from enemy import Enemy
import random

class Necromancer(Enemy):
    """
    This is the boss blueprint 
    """
    def __init__(self, name):
        super().__init__(name)
        self.health = 300

    def RiseOfTheDead(self):
        if self.health < 300:
            print(f"{self.name} summoned the dead! {self.attack_power} damage dealt.")            
            return random.randint(65, 85)

    def DarkMagicProjectile(self):
        if self.health < 250:
            print(f"{self.name} is shooting Dark Magic Projectiles! {self.attack_power} damage dealt.")
            return random.randint(75, 90)
        
    def StinkyCloud(self):
        if self.health < 200:
            print(f"{self.name} casts Stinky Cloud! {self.attack_power} damage dealt.")
            return random.randint(80, 95)
        
    def HealingSpell(self):
        if self.health < 150:
            print(f"{self.name} casts a Healing Spell and restores 30 health! Health is now {self.health}.")
            return self.health + 30

    def DebuffingCurse(self):
        if self.health < 100:
            print(f"{self.name} casts a Debuffing Curse! Your attack dealt 30 less damage. {self.attack_power} damage dealt.")
            return self.damage - 30

    def TheForce(self):
        if self.health < 50:
            print(f"{self.name} uses The Force! {self.attack_power} damage dealt.")
            return random.randint(130, 160)

    def attack(self):
        if self.health < 250:
            self.attack_power = random.randint(85, 100)
        elif self.health < 200:
            self.attack_power = random.randint(100, 115)
        elif self.health < 150:
            self.attack_power = random.randint(115, 130)
        elif self.health < 100:
            self.attack_power = random.randint(130, 145)
        elif self.health < 50:
            self.attack_power = random.randint(145, 160)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
        