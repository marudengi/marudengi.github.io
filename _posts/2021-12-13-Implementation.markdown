---
layout: post
title:  "2. Implementation"
date:   2021-12-15 22:08:00 +0900
categories: Algorithm Theory Implementation Python
---

1. 완전탐색 : 모든 경우의 수를 다 계산하기
2. 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례로 수행

문제를 잘 읽고 순서대로 차분하게 풀면 됨
***

## 2.1 상하좌우

여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N, N) 이다. 여행가 A는 상,하, 좌,우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여있다.
계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D중 하나의 문자가 반복적으로 적혀있다. 이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.

key) 명령을 차례로 수행하므로 시뮬레이션 유형. 

```javascript
N = int(input())
x, y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

move = ['L','R','U','D']

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx > N or nx < 1 or ny > N or ny < 1:
        continue

    x,y = nx, ny

print(x,y)
#=> input 5
#=> input R R R U D D
#=> print 3 4
```

***

## 2.2 시각

정수 N 이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

key) 모든 경우를 다 수행하면 되므로 완전탐색

```javascript
N = int(input())

result = 0

for hour in range(N+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour)+str(minute)+str(second):
                result += 1

print(result)
#=> input 5
#=> print 11475
```
***
## 2.3 왕실의 나이트

8 x 8의 체스판이 있다. 체스판 특정한 칸에 나이트가 있고 L자로 이동 가능하다.(체스에서 나이트의 움직임) 나이트의 시작 위치가 주어질 때 나이트가 이동 가능한 경우의 수를 구하는 프로그램을 작성하시오.

key) 나이트가 움직이는 대로 수행하면 되므로 시뮬레이션 유형. 나이트가 움직이는 방향을 미리 리스트에 넣어놓고 그 방향으로 움직였을 때 체스판을 벗어나는지 확인

```javascript
N = input()

x = ord(N[0]) - 96

y = int(N[1])

moves = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

result = 0

for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    if nx > 8 or nx < 1 or ny > 8 or ny < 1:
        continue
    result += 1

print(result)
#=> input a1
#=> print 2
```
***
## 2.4 게임 개발

게임 캐릭터가 맵에서 움직이는 게임을 개발중이다. 캐릭터가 있는 장소는 1 x 1 크기의 정사각형으로 이루어진 N x M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다. 캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다. 캐릭터는 상하좌우 움직일 수 있고, 바다로 되어있는 공간에는 갈 수 없다.

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례로 갈 곳을 정한다.

2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.

3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

위 과정을 반복적으로 수행했을 때, 캐릭터가 방문한 칸 수를 출력하는 프로그램을 작성하시오.

캐릭터 방향 => 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽

맵 구성 => 0 : 육지, 1 : 바다

key) 정해진 메뉴얼대로 수행하면 되는 문제이므로 시뮬레이션 유형.
방향정보를 x,y좌표로 따로 두개의 리스트로 두어 0,1,2,3 별로 북동남서을 인덱스로 진행한다.
진행 정보를 저장하기 위한 0으로 채운 별도의 맵을 만든다.
방문위치를 1로 채운다.

```javascript
n,m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x,y,direction = map(int, input().split())

d[x][y] = 1

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)

#=> input 4 4
#=> input 1 1 0
#=> input 1 1 1 1
#=> input 1 0 0 1
#=> input 1 1 0 1
#=> input 1 1 1 1
#=> print 3
```
