num = int(input("num: "))
x = 2
pares = 0
control = True
result = False
if num == 1 or num == 0:
    print(f"{num} não é um numero primo")
elif num == 2:
    print(f"{num} é um numero primo")
else:
    while (pares < num):
        if x % 2 == 0:
            pares=pares+1
            print(x)
            if num % x == 0 and control:
                control = False
        x=x+1
        if x == num and control:
            control = False
            result = True
if result == True:
    print(f"{num} é um numero primo")
else:
    print(f"{num} não é um numero primo")