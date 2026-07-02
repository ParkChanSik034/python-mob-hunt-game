import random

class Mob:
  def __init__(self, name, hp, attack_power, defense):
    self.name = name
    self.hp = hp
    self.attack_power = attack_power
    self.defense = defense

  def attack(self):
    print(f"{self.name}이(가) 스킬을 발휘했습니다! {self.attack_power}의 데미지로 공격했습니다.")

  def info(self):
    print(f"---{self.name} 정보---")
    print(f"hp: {self.hp}")
    print(f"attack_power: {self.attack_power}")
    print(f"defense: {self.defense}")

class Mushroom(Mob):
  def run(self): #달리기
    print(f"{self.name}이가 달리기 시작했습니다.")

  def jump(self): #점프
    print(f"{self.name}이가 점프했습니다.")

class Slime(Mob):
    def __init__(self, name, hp, attack_power, defense):
        super().__init__(name, hp, attack_power, defense) # 1. 부모님 거 기본 세팅
        self.count = 1                                    # 2. 그리고 슬라임 전용 'count'도 추가

    def split(self):
      self.count *= 2
      print(f"{self.name}이 증식했습니다. (현재 개수: {self.count} 마리)")

    def info(self):
        super().info()  # 부모 클래스의 info 기본 내용(이름, hp 등) 먼저 출력
        print(f"현재 개수: {self.count}마리")

# ==========================================
# 🎮 시뮬레이션 플레이!
# ==========================================
print("--- 버섯 테스트 ---")
blue_mushroom = Mushroom("파랑버섯", 100, 15, 5)
blue_mushroom.info()
blue_mushroom.attack()
blue_mushroom.run()
blue_mushroom.jump()

red_mushroom = Mushroom("빨간버섯", 200, 25, 5)
red_mushroom.info()
red_mushroom.attack()
red_mushroom.run()
red_mushroom.jump()

print("\n--- 슬라임 테스트 ---")
red_slime = Slime("빨간 슬라임", 150, 20, 8)
red_slime.info()

print("\n--- 슬라임 증식 중 ---")
red_slime.split()  # 1 -> 2마리
red_slime.split()

print("\n--- 증식 후 정보 확인 ---")
red_slime.info()