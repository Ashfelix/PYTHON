n = [2,3,4,5]
l = len(n)
sum = 0
for i in range(l-1):
    for j in range(i+1,l):
        sum += n[i]+n[j]
print(sum)
