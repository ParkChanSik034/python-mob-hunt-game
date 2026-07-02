"hellogit"
class BattleManager:
    def is_monster_dead(self, monster):
        return monster.hp <= 0

    def player_attack(self, player, monster):
        player.attack(monster)

        if self.is_monster_dead(monster):
            print(f"{monster.name}을(를) 처치했습니다!")
        else:
            print(f"{monster.name}의 남은 HP: {monster.hp}")
            