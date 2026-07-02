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
class BattleManager:
    def is_monster_dead(self, monster):
        """몬스터가 죽었는지 확인하는 메서드 (HP가 0 이하인지 체크)"""
        return monster.hp <= 0

    def player_attack(self, player, monster):
        """플레이어가 몬스터를 공격하고 결과를 출력하는 메서드"""
        # 플레이어가 몬스터를 공격 (참고: Player.attack 메서드가 있다고 가정)
        player.attack(monster)

        # 공격 후 몬스터의 상태에 따라 메시지 출력
        if self.is_monster_dead(monster):
            print(f"{monster.name}을(를) 처치했습니다!")
        else:
            print(f"{monster.name}의 남은 HP: {monster.hp}")
            