N = int(input())
l = list(map(int,input().split()))
for i in range(0,N-1):
    temp = 0
    for j in range(i+1,N):
        if l[i] > l[j]:
            temp = l[j]
            l[j] = l[i]
            l[i] = temp

print(l)      

            
