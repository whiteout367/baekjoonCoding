import random

print('10점을 얻거나 벽에 닿으면 종료됩니다.')
print('1:위 2:아래 3:오른쪽 4:왼쪽')
print('0:빈곳 1:먹이 2:나')
weight = int(input('게임장의 넓이:'))
height = int(input('게임장의 높이:'))
board = [[0 for j in range(0, weight)] for i in range(0, height)]

score = 0

#나 처음위치
a = 0
b = 0
board[a][b] = 2

#먹이
food_height = 0
food_weight = 0

def set_food():
    #먹이위치 랜덤
    global food_height, food_weight
    food_height = random.randrange(0,height)
    food_weight = random.randrange(0,weight)
    
    if board[food_height][food_weight] == 2:
        food_height = random.randrange(0,height)
        food_weight = random.randrange(0,weight)
        
    #먹이 위치
    board[food_height][food_weight] = 1

set_food()

if  board[0][0] == 1:
    set_food()
    board[0][0] = 2

while True:
    for i in board:
        print(i)
    direct = int(input('방향 입력:'))
    if direct == 1:
        board[a][b] = 0
        a -= 1
        if 0 > a:
            print('게임판에 닿았습니다. 게임 오버')
            break
        board[a][b] = 2
        
    elif direct == 2:
        board[a][b] = 0
        a += 1
        if a > height - 1:
            print('게임판에 닿았습니다. 게임 오버')
            break
        board[a][b] = 2
    
    elif direct == 3:
        board[a][b] = 0
        b += 1
        if b > weight - 1:
            print('게임판에 닿았습니다. 게임 오버')
            break
        board[a][b] = 2
        
    elif direct == 4:
        board[a][b] = 0
        b -= 1
        if 0 > b:
            print('게임판에 닿았습니다. 게임 오버')
            break
        board[a][b] = 2
        
    if  a == food_height and b == food_weight:
        score += 1
        print('score:', score)
        set_food()
        if score == 10:
            print('축하합니다. 게임에서 이겼습니다.')
            break
        
        
    