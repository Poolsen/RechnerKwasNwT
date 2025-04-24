#utils
import random
for n in range(5):
    quackities = []
    for i in range(26):
        random_number = round(random.uniform(-4, 4),4)
        if abs(random_number) >= 2:
            random_number = round(random.uniform(-4, 4),4)
        quackity = round(99.3237 / (100+random_number),4)
        quackities.append(quackity)

    print(quackities)
    total = 0
    for element in quackities:
        total += element
    print(total/26)
