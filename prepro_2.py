"""X"""
def main():
    """x"""
    money = int(input())
    money_2 = money
    water = int(input())
    snack_val1 = int(input())
    snack_val2 = int(input())
    snack_val3 = int(input())
    money -= water
    snack_1 = money%3
    if snack_1 == 0:
        snack_1 = 10
        result1 = snack_val1*snack_1
    elif snack_1 == 1:
        snack_1 = 15
        result1 = snack_val1*snack_1
    elif snack_1 == 2:
        snack_1 = 20
        result1 = snack_val1*snack_1
    price = snack_val1*snack_1
    money -= price
    snack_2 = money%3
    if snack_2 == 0:
        snack_2 = 12
        result2 = snack_val2*snack_2
    elif snack_2 == 1:
        snack_2 = 15
        result2 = snack_val2*snack_2
    elif snack_2 == 2:
        snack_2 = 18
        result2 = snack_val2*snack_2
    price = snack_val2*snack_2
    money -= price
    snack_3 = money%3
    if snack_3 == 0:
        snack_3 = 5
        result3 = snack_val3*snack_3
    elif snack_3 == 1:
        snack_3 = 7
        result3 = snack_val3*snack_3
    elif snack_3 == 2:
        snack_3 = 9
        result3 = snack_val3*snack_3
    price = snack_val3*snack_3
    money -= price
    if money >= 0:
        print("Now you have %d left." %money)
        print("Here's your order!")
        print("Water: %d baht" %water)
        print("Snack number 1: %d baht\nSnack number 2: %d \
baht\nSnack number 3: %d baht" %(result1, result2, result3))
    elif money < 0:
        print("Now you have %d left." %money_2)
        print("You don't have enough money!")
main()
