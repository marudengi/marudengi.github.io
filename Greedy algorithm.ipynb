{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1. 그리디 알고리즘"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> 요약<br>\n",
    "1. 현재 상황에서 가장 좋은것을 고르는 것\n",
    "2. 따라서 현재 가장 좋아 보이는 것을 선택했을 때 해결되는 문제인가 파악 능력 필요\n",
    "3. \"기준\"을 잘 파악해야함('가장 큰 순서대로','가장 작은 순서대로')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1-1 거스름돈"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> 수중에 500원,100원, 50원, 10원 이 있고 N원을 받았을때 거슬러 주는 최소 동전의 갯수<br> (N은 10의 배수)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> key) 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로<br> 작은 단위의 동전들을 종합해 다른 해가 나올 수 없다.\n",
    "\n",
    "> 즉 화폐 단위가 무작위로 주어진다면 그리디 알고리즘으로 해결 불가"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "n = 1260\n",
    "count = 0\n",
    "\n",
    "coin_types = [500,100,50,10]\n",
    "\n",
    "for coin in coin_types:\n",
    "    count += n // coin\n",
    "    n %= coin\n",
    "    \n",
    "print(count)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1-2 큰수의 법칙"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> 다양한 수로 이루어진 N 크기의 배열, 그 수들을 M번 더하여 가장 큰 수 만들기<br>\n",
    "(배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과해서 더해질 수 없다.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> key) 가장 큰 수로 k번 더하고 한번씩 두번째로 큰 수를 더해주는 것을 M번 반복"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 8 3\n",
      "2 4 5 4 6\n",
      "46\n"
     ]
    }
   ],
   "source": [
    "n, m, k = map(int, input().split())\n",
    "data = list(map(int, input().split()))\n",
    "\n",
    "data.sort()\n",
    "\n",
    "first = data[n-1]\n",
    "second = data[n-2]\n",
    "\n",
    "result = 0\n",
    "\n",
    "while True:\n",
    "    for i in range(k):\n",
    "        if m == 0:\n",
    "            break\n",
    "        result += first\n",
    "        m -= 1\n",
    "    if m == 0:\n",
    "        break\n",
    "    result += second\n",
    "    m -= 1\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 8 3\n",
      "2 4 5 4 6\n",
      "46\n"
     ]
    }
   ],
   "source": [
    "#solution2\n",
    "n, m, k = map(int,input().split())\n",
    "data = list(map(int,input().split()))\n",
    "\n",
    "data.sort()\n",
    "\n",
    "first = data[n-1]\n",
    "second = data[n-2]\n",
    "\n",
    "result = 0\n",
    "\n",
    "count = int(m/(k+1))*k\n",
    "count += m%(k+1)\n",
    "\n",
    "result += (count)*first\n",
    "result += (m-count)*second\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1-3 숫자카드게임"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> 여러 숫자 카드중 가장 높은 수를 뽑는 게임\n",
    "1. 카드가 NxM형태로 놓여있음\n",
    "2. 뽑으려는 행 선택\n",
    "3. 행에 포함된 카드 중 가장 작은 숫자 카드 뽑기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> key) 각 행마다 가장 작은수를 찾고 그 중 가장 큰 수를 찾기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 3\n",
      "3 1 2\n",
      "4 1 4\n",
      "2 2 2\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "n, m = map(int, input().split())\n",
    "result = 0\n",
    "\n",
    "for i in range(n):\n",
    "    data = list(map(int,input().split()))\n",
    "    min_value = min(data)\n",
    "    result = max(result, min_value)###\n",
    "    \n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1-4 1이 될 때까지"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> N이 1이 될 때까지 다음 과정을 수행\n",
    "1. N에서 1을 뺀다.\n",
    "2. N을 K로 나눈다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> key) 최대한 많이 나누기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25 5\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "n, k = map(int, input().split())\n",
    "\n",
    "result = 0\n",
    "\n",
    "while True:\n",
    "    target = (n//k)*k\n",
    "    result += (n-target)\n",
    "    n = target\n",
    "    \n",
    "    if n < k:\n",
    "        break\n",
    "    result += 1\n",
    "    n //= k\n",
    "    \n",
    "result += (n - 1)\n",
    "print(result)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
