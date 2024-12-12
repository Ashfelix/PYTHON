def happy_numbers(n):
    past = set()			
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        print(n)
        break
print(happy_numbers(3))

