from coffee_machine import *

# 메뉴 입력란
is_on = True
while is_on:
    choice = input("어떤 커피를 원하세요? (아메리카노 / 카페라떼 / 카푸치노) >> ")

    if choice == "아메리카노" or choice == "카페라떼" or choice == "카푸치노":
        # 재료 충분여부 조회
        input_menu = return_english(choice)
        if enough_ingredients(input_menu) == False:  # 없을때
            is_on = False
        else:  # 있을 때
            # 메뉴 입력받고 돈 확인만
            while (True):
                print(f"{choice}를 선택하셨습니다. ")
                pay_to_money = 0

                pay_to_money = MENU[input_menu]["cost"]

                print(f"가격은 {pay_to_money}원 입니다")
                # 재료 계산 여기서
                use_ingredients(input_menu)
                # 돈 실제 지불확인
                pay_money(pay_to_money, choice)
                break  # 안쪽 while 반복종료
            bl = input("더 주문하시겠습니까? (Y/N) >> ")
            if bl == "N":
                print("안녕히가세요")
                break  # 프로그램 종료
            else:
                continue
    elif choice == "off":
        is_on = False
        print("종료합니다")
    elif choice == "report":
        now_report()
    else:
        print("없는 메뉴를 입력하셨습니다")