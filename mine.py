import random

Questionsmuch = int(input("Сколько примеров задать?: "))
Questions = 0
good = 0
bad = 0

while True:
    first_num = random.randrange(1, 10)
    secend_num = random.randrange(1, 10)

    answer = int(input(f"{first_num} * {secend_num} = "))
    control = first_num * secend_num

    if answer == control:
        good += 1
        Questions += 1

    if answer != control:
        bad += 1
        Questions += 1

    if Questions == Questionsmuch:
        print("==================================")
        print(f"Задано примеров: {Questionsmuch}")
        print(f"Ваши правильные ответы: {good}")
        print(f"Ваши неправильные ответы: {bad}")
        print("==================================")
        break

input()