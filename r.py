# import random

import random
r = random.randint(1, 100)
while True:
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('恭喜你猜對了!')
        break
    elif num > r:
        print('比答案大')
    else:
        print('比答案小')
