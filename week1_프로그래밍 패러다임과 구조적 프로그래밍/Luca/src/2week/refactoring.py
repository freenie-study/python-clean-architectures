# =============================================================
# ======================= 1. 구구단 출력기 =======================
# =============================================================
class Game:
    def __init__(self) -> None:
        # 메뉴 옵션
        self.options = 'main', '1', '2', '3', 'q'
        self.menu = ''
        self.EOL = '\n\n'
        self.quit = '[q: 나가기]>> '

        # 에러 메시지 옵션
        self.msg_error = '오류! 입력값이 조건에 맞지 않습니다. 다시 입력해주세요! (1 ~ 9)'
        self.msg_bye = '구구단을 종료합니다. 이용해주셔서 감사합니다.'


class MultiplicationTablesGame(Game):
    def __init__(self) -> None:
        super().__init__()
        # 구구단 옵션
        self.min_dan = 1
        self.max_dan = 10

    def play(self):
        while self.menu != self.options[-1]:
            self.menu = self.options[0]  # 메인
            if self.menu == self.options[0]:
                print("""
                구구단 출력기
                ----------------------------------------------------------------------
                        1) n단 출력    2) n단까지 출력   3) n ~ m단 출력   q) 나가기
                ----------------------------------------------------------------------
                """)
                self.menu = input("메뉴를 선택하세요>> ")
                print()

                if self.menu not in self.options:
                    print(f'입력값 = {self.menu}\n메뉴를 잘못 입력하셨습니다. 다시 입력하세요.', end=self.EOL)
                else:
                    n, m = '', ''
                    while n != self.options[-1] or m != self.options[-1]:
                        # n단
                        if self.menu == self.options[1]:
                            n = input(f'몇 단을 출력하시겠습니까? {self.quit}')  # n = 'q'
                            m = n  # m = 'q'

                        # ~ n단
                        elif self.menu == self.options[2]:
                            n = str(self.min_dan)
                            m = input(f'몇 단까지 출력하시겠습니까? {self.quit}')

                        # n ~ m단
                        elif self.menu == self.options[3]:
                            n = input(f'시작 단을 입력하세요(1 ~ 9) {self.quit}')
                            if n.lower() == 'q':
                                print(self.msg_bye)
                                return
                            m = input(f'끝 단을 입력하세요({n} ~ 9) {self.quit}')
                        else:  # self.menu == q
                            break  # 아래 코드를 타지 못하게

                        ### 결과물 출력 ###
                        if self.options[-1] in [n, m]:
                            self.menu = self.options[-1]
                        else:
                            boundary = [str(i) for i in range(self.min_dan, self.max_dan)]
                            if (n in boundary) and (m in boundary):
                                n, m = int(n), int(m)
                                if n <= m:
                                    # 정상적으로 구구단 출력하기
                                    for dan in range(n, m + 1):
                                        print(f"=== {dan}단 ===")
                                        for i in range(self.min_dan, self.max_dan):
                                            print(f'{dan} X {i} = {int(dan) * i}')
                                else:
                                    print(self.msg_error)
                                    continue
                                # 메인 메뉴로 이동
                                self.menu = self.options[0]
                            else:
                                print(self.msg_error)
        else:
            print(self.msg_bye)
            return

# 문제점: 메뉴3에서 n에 q가 입력되어도 바로 끝나지 않고 m을 입력받은 뒤에 끝남.

if __name__ == '__main__':
    game = MultiplicationTablesGame()
    game.play()
