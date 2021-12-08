num = int(input("num: "))
x = 2
if num == 1 or num == 0:
    print(f"{num} não é um numero primo")
elif num == 2:
    print(f"{num} é um numero primo")
else:
    while (x < num):
        if x % 2 == 0:
            if num % x == 0:
                print(f"{num} não é um numero primo")
                break
        x=x+1
        if x == num:
            print(f"{num} é um numero primo")