# coding:utf-8
inputs = input().split()
N = int(inputs[0])
K = int(inputs[1])
pic = []
r = []
for _ in range(N):
    pic.append(input().split)
def resize(k,x,y):
    result = 0
    for i in range(k):
        for j in range(k):
            result += pic[i+x][j+y]
            avg = result/k/k
    return avg

for i in range(0,N,K):
    result1 = ''
    for j in range(0,N,K):
        result1 += str(resize(K,i,j)) + ' '
    r.append(result1.rstrip(' '))
for i in r:
    print(i)
