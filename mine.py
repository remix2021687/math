import random

whiles = True
good = 0
bad = 0

while whiles:
    first_num = random.randrange(1, 10)
    secend_num = random.randrange(1, 10)


    answer = int(input(f"{first_num} * {secend_num} = "))
    control = first_num * secend_num

    if answer == control:
        good += 1

    if answer == "Exit":
        whiles = False



print(f"Ваши правильные ответы: {good}")
print(f"Ваши неправильные ответы: {bad}")

input()

print(f"{type(good)}, {good}")