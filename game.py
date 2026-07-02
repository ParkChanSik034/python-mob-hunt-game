from player import Player
from monster import Mushroom, Slime

class Game:
    def __init__(self, player, monster, battle_manager=None):
        """
        게임 생성자
        :param player: Player 객체
        :param monster: 몬스터 객체 (Mushroom 또는 Slime 등)
        :param battle_manager: 배틀 매니저 (기본값 None)
        """
        self.player = player
        self.monster = monster
        self.battle_manager = battle_manager

    def show_menu(self):
        """
        메뉴를 출력하는 메서드
        """
        print("\n" + "=" * 30)
        print("1. 공격하기")
        print("2. 플레이어 정보 보기")
        print("3. 몬스터 정보 보기")
        print("4. 종료")
        print("=" * 30)

    def start(self):
        """
        게임을 시작하고 메뉴를 실행하는 메서드
        """
        print("🎮 몹 잡기 게임을 시작합니다!")
        
        while True:
            self.show_menu()
            choice = input("선택할 메뉴 번호를 입력하세요: ").strip()
            
            if choice == "1":
                self.player.attack(self.monster)
                if self.monster.hp <= 0:
                    print(f"🎉 몬스터 {self.monster.name}을(를) 처치했습니다! 게임을 종료합니다.")
                    break
            elif choice == "2":
                self.player.info()
            elif choice == "3":
                self.monster.info()
            elif choice == "4":
                print("👋 게임을 종료합니다. 다음에 또 만나요!")
                break
            else:
                print("❌ 잘못된 입력입니다. 1~4 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    # 게임 테스트용 초기화 및 실행
    # (monster.py 임포트 시 monster.py 내부의 테스트 코드 출력물이 먼저 실행됩니다)
    player = Player("용사", 100, 30)
    monster = Slime("슬라임", 50, 10, 5)
    
    game = Game(player, monster)
    game.start()