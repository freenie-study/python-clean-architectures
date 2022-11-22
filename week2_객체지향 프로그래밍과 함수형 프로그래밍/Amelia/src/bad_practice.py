# =============================================================
# ======================= 1. 구구단 출력기 =======================
# =============================================================


# 메뉴 옵션
options = 'main', '1', '2', '3', 'q'
menu = ''
EOL = '\n\n'
quit = '[q: 나가기]>> '

# 구구단 옵션
min_dan = 1
max_dan = 10

# 에러 메시지 옵션
msg_error = '오류! 입력값이 조건에 맞지 않습니다. 다시 입력해주세요! (1 ~ 9)'
msg_bye = '구구단을 종료합니다. 이용해주셔서 감사합니다.'

while menu != options[-1]:
    menu = options[0]  # 메인
    if menu == options[0]:
        print("""
        구구단 출력기
        ----------------------------------------------------------------------
                   1) n단 출력    2) n단까지 출력   3) n ~ m단 출력   q) 나가기
        ----------------------------------------------------------------------
        """)
        menu = input("메뉴를 선택하세요>> ")
        print()

        if menu not in options:
            print(f'입력값 = {menu}\n메뉴를 잘못 입력하셨습니다. 다시 입력하세요.', end=EOL)
        else:
            n, m = '', ''
            while n != options[-1] or m != options[-1]:
                # n단
                if menu == options[1]:
                    n = input(f'몇 단을 출력하시겠습니까? {quit}')  # n = 'q'
                    m = n  # m = 'q'

                # ~ n단
                elif menu == options[2]:
                    n = str(min_dan)
                    m = input(f'몇 단까지 출력하시겠습니까? {quit}')

                # n ~ m단
                elif menu == options[3]:
                    n = input(f'시작 단을 입력하세요(1 ~ 9) {quit}')
                    m = input(f'끝 단을 입력하세요({n} ~ 9) {quit}')
                else:  # menu == q
                    break  # 아래 코드를 타지 못하게

                ### 결과물 출력 ###
                if options[-1] in [n, m]:
                    menu = options[-1]
                else:
                    boundary = [str(i) for i in range(min_dan, max_dan)]
                    if (n in boundary) and (m in boundary):
                        n, m = int(n), int(m)
                        if n <= m:
                            # 정상적으로 구구단 출력하기
                            for dan in range(n, m + 1):
                                print(f"=== {dan}단 ===")
                                for i in range(min_dan, max_dan):
                                    print(f'{dan} X {i} = {int(dan) * i}')
                        else:
                            print(msg_error)
                            continue
                        # 메인 메뉴로 이동
                        menu = options[0]
                    else:
                        print(msg_error)
else:
    print(msg_bye)

# 문제점: 메뉴3에서 n에 q가 입력되어도 바로 끝나지 않고 m을 입력받은 뒤에 끝남.