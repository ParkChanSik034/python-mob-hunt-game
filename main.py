from player import Player
from monster import Mushroom
from battle import BattleManager
from game import Game

def main():
    # 1. 플레이어 생성 (Player)
    # player.py의 Player 클래스를 사용합니다.
    player = Player(name="용사", hp=100, attack_power=25)

    # 2. 몬스터 생성 (BlueMushroom)
    # monster.py에는 별도의 BlueMushroom 클래스가 존재하지 않고 Mushroom 클래스가 정의되어 있습니다.
    # monster.py 내부의 테스트 케이스를 참고하여 파랑버섯 객체를 생성합니다.
    blue_mushroom = Mushroom(name="파랑버섯", hp=80, attack_power=15, defense=5)

    # 3. 배틀 매니저 생성 (BattleManager)
    # battle.py의 BattleManager 클래스를 사용합니다.
    battle_manager = BattleManager()

    # 4. 게임 객체 생성 및 시작 (Game)
    # game.py의 Game 클래스를 사용하며, 생성 시 player, monster, battle_manager를 주입합니다.
    game = Game(player=player, monster=blue_mushroom, battle_manager=battle_manager)
    game.start()

if __name__ == "__main__":
    main()