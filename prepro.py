"""x"""
def main():
    '''X'''
    point = float(input())
    if point < 1.00:
        print("I'm so sad.")
    elif point < 2.00:
        point_2 = 4-point
        print("%.2f" %point_2)
    elif point >= 2.00:
        print("I'm so happy.")
main()
