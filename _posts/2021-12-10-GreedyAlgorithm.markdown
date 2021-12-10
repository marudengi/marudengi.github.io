---
layout: post
title:  "1. Greedy Algorithm"
date:   2021-12-10 14:28:09 +0900
categories: Algorithm Theory Greedy Python
---

* 현재 상황에서 가장 좋은것을 고르는 것
* 따라서 현재 가장 좋아보이는 것을 선택했을 때 해결되는 문제인가 파악 능력 필요
* "기준"을 잘 파악해야함('가장 큰 순서대로','가장 작은 순서대로')

***

## 1.1 거스름돈

수중에 500원,100원, 50원, 10원 이 있고 N원을 받았을때 거슬러 주는 최소 동전의 갯수
(N은 10의 배수)

key) 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로
작은 단위의 동전들을 종합해 다른 해가 나올 수 없다.

즉 화폐 단위가 무작위로 주어진다면 그리디 알고리즘으로 해결 불가

```javascript
n = 1260
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    count += n // coin
    n %= coin
    
print(count)
#=> print 6
```

***

## 1.2 큰수의 법칙

다양한 수로 이루어진 N 크기의 배열, 그 수들을 M번 더하여 가장 큰 수 만들기
(배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과해서 더해질 수 없다.)

key) 가장 큰 수로 k번 더하고 한번씩 두번째로 큰 수를 더해주는 것을 M번 반복

```javascript
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)
#=> input 5 8 3
#=> input 2 4 5 4 6
#=> print 46
```

## 1.3 숫자 카드 게임

여러 숫자 카드중 가장 높은 수를 뽑는 게임

1. 카드가 NxM형태로 놓여있음
2. 뽑으려는 행 선택
3. 행에 포함된 카드 중 가장 작은 숫자 카드 뽑기

key) 각 행마다 가장 작은수를 찾고 그 중 가장 큰 수를 찾기

```javascript
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result, min_value)###
    
print(result)
#=> input 3 3
#=> input 3 1 2
#=> input 4 1 4
#=> input 2 2 2
#=> print 2
```

## 1.4 1이 될 때까지

N이 1이 될 때까지 다음 과정을 수행

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

key) 최대한 많이 나누기

```javascript
n, k = map(int, input().split())

result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    
    if n < k:
        break
    result += 1
    n //= k
    
result += (n - 1)
print(result)

#=> input 25 5
#=> print 2
```

백준 > [그리디 알고리즘][greedy-algorithm]

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
[greedy-algorithm]: https://