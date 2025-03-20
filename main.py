import random

print("Введите первое значение")
value1 = int(input())
print("Введите второе значение")
value2 = int(input())

value3 = random.randint(value1, value2)

while True:
    answer = input("Введите чет/нечет")
    if answer == "чет" and value3 % 2 == 0:
        print("Ты победил тигр")
        break
    elif answer == "нечет" and value3 % 2 == 0:
        print("Ты не победил")
    elif answer == "нечет" and value3 % 2 != 0:
        print("Ты победил тигр")
        break
    elif answer == "чет" and value3 % 2 != 0:
        print("Ты не победил")    
    else:
        print("Ты имплант") 