MENU = {
    "americano": {
        "ingredients": {
            "water": 250,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1500,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2500,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3000,
    }
}

# 자판기에 있는 재료 자원
resources = {
    "water": 700,
    "milk": 300,
    "coffee": 200,
}

# 프로그램 종료
# def program_off():
#     exit()

# 재료 충분여부 파악


def enough_ingredients(choice):
    bools = False
    orders = MENU[choice]["ingredients"]
    for item in orders:
        if resources[item] < orders[item]:  # 물비교
            # 재료 - 물이 메뉴의 물보다 작으면 ( =/=같으면, 이유는 같으면 사용가능함)
            print(f"{item}이 부족합니다.")
            bools = False
        else:
            bools = True

    if bools:
        return True
    else:
        print("안녕히가세요.")
        exit()
# ----------------------------------------------------------------------------------------

# 재료 사용


def use_ingredients(input_val):  # 메뉴명 입력, 영어로 들어옴
    resources['water'] -= MENU[input_val]["ingredients"]['water']  # 물계산
    resources['milk'] -= MENU[input_val]["ingredients"]['milk']  # 우유계산
    resources['coffee'] -= MENU[input_val]["ingredients"]['coffee']  # 커피계산

# 현재 재고


def now_report():
    print(
        f"현재 남은 재료입니다. 물 : {resources['water']}ml, 우유 : {resources['milk']}ml, 커피 : {resources['coffee']}g")
    enough_ingredients()

# 메뉴명 영어 치환 리턴


def return_english(input_val):
    if input_val == "아메리카노":
        return "americano"
    elif input_val == "카페라떼":
        return "latte"
    elif input_val == "카푸치노":
        return "cappuccino"


# 수익
profit = 0

def pay_money(pay_to_money, choice):
    cost = 0
    while (True):
        get_money = input("돈을 지불 해주세요. >> ")
        cost = cost + int(get_money)

        if cost == pay_to_money:  # 같을경우
            print("알맞게 지불하셨습니다.")
            print(f"주문하신 {choice} 나왔습니다. 안녕히가세요.")
            break
        elif cost > pay_to_money:  # 클 경우
            print(f"총 {cost}원 받았습니다.")
            print(f"거스름돈 {cost - pay_to_money}원 입니다.")
            print(f"주문하신 {choice} 나왔습니다. 안녕히가세요.")
            break
        else:  # 작을 경우
            print(f"총 {cost}원 받았습니다.")
            print(f"{pay_to_money - cost}원 부족합니다. 지불해주세요")

    global profit
    profit += pay_to_money  # 수익
    print(f"판매수익 : {profit}")
# ----------------------------------------------------------------------------------------


