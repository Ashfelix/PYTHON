class Parent:
    def __init__(self,n):
        self.n = n
class Child(Parent):
    def __init__(self):
        pass
    def fun(self):
            string =str(self.n)
            digits = [int(i) for i in string]
            k = len(digits)
            sum = 0
            for a in range(k-1):
                for b in range(a+1,k):
                    sum+=digits[a]+digits[b]
            print(sum)
if __name__ == "__main__":
    child = Child()
    child.n = int(input())
    child.fun()
            
            
        
    
        
