import random
lottery_num = range(1,49)
for _ in range(5):
    win_num = random.sample(lottery_num,6)
    win_num.sort()
    print(win_num)
