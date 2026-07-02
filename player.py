class Player:
    def __init__(self, name, hp, attack_power):
        """
        플레이어 생성자
        :param name: 플레이어 이름 (str)
        :param hp: 플레이어 체력 (int)
        :param attack_power: 플레이어 공격력 (int)
        """
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, monster):
        """
        몬스터를 공격하여 몬스터의 HP를 감소시키는 메서드
        데미지 공식 = 플레이어 공격력 - 몬스터 방어력 (최소 1 보장)
        """
        # 데미지 계산: 플레이어 공격력 - 몬스터 방어력
        # monster 객체에 defense 속성이 있다고 가정합니다.
        damage = self.attack_power - monster.defense
        
        # 데미지가 1보다 작으면 최소 1로 처리
        if damage < 1:
            damage = 1
            
        # 몬스터의 HP 감소 (monster 객체에 hp 속성이 있다고 가정합니다.)
        monster.hp -= damage
        
        print(f"⚔️ {self.name}(이)가 몬스터를 공격하여 {damage}의 데미지를 입혔습니다!")

    def info(self):
        """
        플레이어의 현재 상태를 출력하는 메서드
        """
        print("-" * 30)
        print(f"[ 플레이어 상태 ]")
        print(f"👤 이름: {self.name}")
        print(f"❤️ HP: {self.hp}")
        print(f"⚔️ 공격력: {self.attack_power}")
        print("-" * 30)