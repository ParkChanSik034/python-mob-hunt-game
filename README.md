# 🎮 Python 몹 잡기 게임 (python-mob-hunt-game)

## 프로젝트 소개
본 프로젝트는 Python 클래스 상속(Class Inheritance) 실습을 통해 구현한 몬스터 클래스들을 기반으로, 플레이어와 몬스터가 상호작용하는 터미널 기반 텍스트 RPG 게임입니다. 객체 지향 프로그래밍(OOP) 및 다양한 협업 툴 학습을 목적으로 개발되었습니다.

---

## 주요 기능
* **인터랙티브 터미널 메뉴**: 텍스트 GUI를 통해 공격, 상태 보기, 종료 작업을 간단히 제어할 수 있습니다.
* **클래스 상속 기반 몬스터**: `Mob` 부모 클래스를 상속받은 `Mushroom`(버섯) 및 `Slime`(슬라임) 등 고유 기능을 가진 몬스터들이 동작합니다.
* **전투 시스템 & 매니저**: `BattleManager`를 통한 몬스터 체력 상태 감지 및 전투 결과 출력을 수행합니다.
* **방어력 및 최소 데미지 공식**: `데미지 = 공격력 - 방어력 (최소 1 보장)` 공식을 적용해 실감 나는 전투 계산을 진행합니다.

---

## 프로젝트 구조
```text
python-mob-hunt-game/
├── main.py          # 게임의 진입점 (Entry Point)으로 객체 생성 및 실행 담당
├── game.py          # 전체 게임 흐름 제어 및 메뉴 출력 (Game 클래스)
├── player.py        # 플레이어 캐릭터 모델 및 공격 메서드 (Player 클래스)
├── monster.py       # 몬스터 모델 (Mob 부모 클래스 및 Mushroom, Slime 자식 클래스)
└── battle.py        # 전투 결과 판정 및 사망 체크 (BattleManager 클래스)
```

---

## 설치 방법
1. **Python 설치**: Python 3.8 이상 버전이 설치되어 있어야 합니다.
2. **저장소 클론**:
   ```bash
   git clone https://github.com/ParkChanSik034/python-mob-hunt-game.git
   cd python-mob-hunt-game
   ```

---

## 실행 방법
터미널에서 아래 명령어를 실행하여 게임을 시작합니다.
```bash
python main.py
```

---

## 팀원 역할
* **정지윤 (Player 담당)**: `player.py`에서 플레이어 생성, 공격 메서드, 데미지 공식 및 상태 출력 구현
* **조율리 (Monster 담당)**: `monster.py`에서 상속 구조를 이용한 `Mob` 부모 클래스 및 `Mushroom`, `Slime` 자식 클래스 기믹 구현
* **김동욱 (Battle 담당)**: `battle.py`에서 전투 판정 및 몬스터 생사 체크를 위한 `BattleManager` 구현
* **박찬식 (Game & Main 담당)**: `game.py`와 `main.py`를 구현하고 각 팀원들의 코드를 연결하여 터미널 게임 완성

---

## AI Agent 활용
* **Antigravity AI Agent**와의 페어 프로그래밍을 통해 `game.py` 내부의 인터랙티브한 CLI 루프와 예외 입력을 처리하는 로직을 효율적으로 설계했습니다.
* 구현 단계 이후 완료 조건을 기반으로 한 다각도 코드 검수를 통해 미작동 요소를 사전에 차단하였습니다.

---

## 향후 개선 사항
* **슬라임 증식 기믹의 전투 반영**: `Slime` 클래스의 `split()` 메서드를 실제 배틀 메뉴 턴에 유기적으로 병합
* **버섯 점프/달리기 기믹의 전투 반영**: `Mushroom` 클래스의 `jump()`, `run()` 스킬을 전투 시 회피 또는 특수 공격으로 구현
* **성장 시스템**: 몬스터 사냥 성공 시 플레이어가 경험치와 골드를 획득하고 레벨 업하는 기능 추가
