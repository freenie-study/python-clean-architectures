# =============================================================
# ======================= 1. 구구단 출력기 =======================
# =============================================================



class GuGuDan:
    def __init__(self):
        self.min_dan = 1
        self.max_dan = 10
        self.options = ['main', '1', '2', '3', 'q']
        self.quit = '[q: 나가기]>>'
        self.msg_error = '오류! 입력값이 조건에 맞지 않습니다. 다시 입력해주세요! (1 ~ 9)'
        self.msg_bye = '구구단을 종료합니다. 이용해주셔서 감사합니다.'
        self.EOL = '\n\n'

    def print_gugudan(self, n, m):
        for dan in range(n, m + 1):
            print(f"=== {dan}단 ===")
            for i in range(self.min_dan, self.max_dan):
                print(f'{dan} X {i} = {int(dan) * i}')

    def run(self):
        while menu != self.options[-1]:
            menu = self.options[0]  # 메인
            if menu == self.options[0]:
                print("""
                구구단 출력기
                ----------------------------------------------------------------------
                           1) n단 출력    2) n단까지 출력   3) n ~ m단 출력   q) 나가기
                ----------------------------------------------------------------------
                """)
                menu = input("메뉴를 선택하세요>> ")
                print()

                if menu not in self.options:
                    print(f'입력값 = {menu}\n메뉴를 잘못 입력하셨습니다. 다시 입력하세요.', end=self.EOL)
                else:
                    n, m = '', ''
                    while n != self.options[-1] or m != self.options[-1]:
                        # n단
                        if menu == self.options[1]:
                            n = input(f'몇 단을 출력하시겠습니까? {self.quit}')  # n = 'q'
                            m = n  # m = 'q'

                        # ~ n단
                        elif menu == self.options[2]:
                            n = str(self.min_dan)
                            m = input(f'몇 단까지 출력하시겠습니까? {self.quit}')

                        # n ~ m단
                        elif menu == self.options[3]:
                            n = input(f'시작 단을 입력하세요(1 ~ 9) {quit}')
                            m = input(f'끝 단을 입력하세요({n} ~ 9) {quit}')
                        else:  # menu == q
                            break  # 아래 코드를 타지 못하게

                        ### 결과물 출력 ###
                        if self.options[-1] in [n, m]:
                            menu = self.options[-1]
                        else:
                            boundary = [str(i) for i in range(self.min_dan, self.max_dan)]
                            if (n in boundary) and (m in boundary):
                                n, m = int(n), int(m)
                                if n <= m:
                                    # 정상적으로 구구단 출력하기
                                    self.print_gugudan(n, m)
                                else:
                                    print(self.msg_error)
                                    continue
                                # 메인 메뉴로 이동
                                menu = self.options[0]
                            else:
                                print(self.msg_error)
        else:
            print(self.msg_bye)
