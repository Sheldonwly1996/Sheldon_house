import random

#设定游戏场景范围
game_range = []
for x in range(11):
    for y in range(11):
        game_range.append((x,y))
length = len(game_range)

#设定乌龟类和鱼类
class Turtle:
    def __init__(self):
        self.health = 100
        self.speed = random.randint(1,2)
        self.address = game_range[random.randint(1,length-1)]

class Fish:
    def __init__(self):
        self.speed = 1
        self.address = game_range[random.randint(1,length-1)]


#设定乌龟和鱼的初始数量，并显示初始坐标
tt = Turtle()
f_1 = Fish()
f_2 = Fish()
f_3 = Fish()
f_4 = Fish()
f_5 = Fish()
f_6 = Fish()
f_7 = Fish()
f_8 = Fish()
f_9 = Fish()
f_10 = Fish()
f = [f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9,f_10]
num = len(f)
f_address ={}

print("初始位置:\n乌龟：",tt.address)
for count in range(10):
    f_address[f[count]] = game_range.index(f[count].address)
    print("鱼"+ str(count) + '：',f[count-1].address)

#设定乌龟和鱼的活动
while tt.health  and num:
   
    steps_big = [-1,1,-2,2,11,-11,22,-22]
    steps_small = [-1,1,11,-11]
    
    # 设定乌龟的运动状态
    # 乌龟到最上方
    if tt.address[0] == 0:
        tt.address = game_range[game_range.index(tt.address)+11]
        tt.health -= 1

    # 乌龟到最下方
    elif tt.address[0] == 10:
        tt.address = game_range[game_range.index(tt.address)-11]
        tt.health -= 1

    # 乌龟到最左方
    elif tt.address[1] == 0:
        address = game_range[game_range.index(tt.address)+1]
        tt.health -= 1

    #乌龟到最右方
    elif tt.address[1] == 10:
        tt.address = game_range[game_range.index(tt.address)-1]
        tt.health -= 1
        
    #乌龟快要撞到墙
    elif tt.address[0] == 1 or tt.address[0] == 9 or tt.address[1] == 1 or tt.address[1] == 9:
        tt.address = game_range[game_range.index(tt.address)+random.choice(steps_small)]
        tt.health -= 1
        
    #其他状况
    else:     
        tt.address = game_range[game_range.index(tt.address)+random.choice(steps_big)]
        tt.health -= 1

    #设定鱼的运动状态
    for count in range(num-1):
        # 鱼到最上方
        if f[count].address[0] == 0:
            f[count].address = game_range[game_range.index(f[count].address)+11]

        # 鱼到最下方
        elif f[count].address[0] == 10:
            f[count].address = game_range[game_range.index(f[count].address)-11]

        # 鱼到最左方
        elif f[count].address[1] == 0:
            f[count].address = game_range[game_range.index(f[count].address)+1]

        # 鱼到最右方
        elif f[count].address[1] == 10:
            f[count].address = game_range[game_range.index(f[count].address)-1]
        # 其他状况
        else:
            f[count].address = game_range[game_range.index(f[count].address)+random.choice(steps_small)]

    #乌龟吃鱼的判定

    for count in range(num-1):
        if tt.address == f[count].address:
            tt.health += 20
            num -= 1
            print('有一条鱼儿被吃掉了！')
            del f[count]
        else:
            continue

    if tt.health == 0:
        print("乌龟输了")
        print("乌龟的坐标：",tt.address)
    elif num == 0:
        print("乌龟赢了")
        print("乌龟的坐标：",tt.address)
        
    else:
        continue

        
        












