from enemy import Enemy

class baby_elf(Enemy):
    #a new special ability
    def cry():
        print("Waaah! Waaah!")

    #overriding the take_damage
    def take_damage(self, damage):
        print("Why are you attacking a baby elf? (╥_╥)")
        return super().take_damage(damage)