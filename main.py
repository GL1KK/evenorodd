import random

print("Введите первое значение")
value1 = int(input())
print("Введите второе значение")
value2 = int(input())

value3 = random.choice([value1, value2])

answer = input("Введите чет/нечет")

if answer == "чет" and value3 % 2 == 0:
    print("Ты победил тигр")
elif answer == "нечет" and value3 % 2 == 0:
    print("Ты не победил")
elif answer == "нечет" and value3 % 2 != 0:
    print("Ты победил тигр")
elif answer == "чет" and value3 % 2 != 0:
    print("Ты не победил")    
else:
    print("Ты имплант") 