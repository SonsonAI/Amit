class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        print("Summation 2 numbers: ", (self.num1 + self.num2))
    def diff(self):
        print("Diff 2 numbers: ", (self.num1 - self.num2))
    def multi(self):
        print("Multi 2 numbers: ", (self.num1 * self.num2))
    def div(self):
        if self.num2 == 0:
            print("Mathematical Error")
        print("Div 2 numbers: ", (self.num1 / self.num2))
x= Calculator(8,4)
x.sum()
x.diff()
x.multi()
x.div()
#########################################
class FacNum:
    def __init__(self,num):
      self.num = num
           
    def factorial(self):
        if self.num == 0:
            return 0
        if self.num == 1:
            return 1
        return self.num * FacNum(self.num - 1).factorial()

x = FacNum(5)
x.factorial()
########################################
class PrimeNum:
    def __init__(self,num):
        self.num = num
    def isPrime(self):
        for i in range(2, self.num):
            if self.num % i == 0:
                return False
        return True
x = PrimeNum(2)
x.isPrime()
######################################
class Dividors:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2        
    def dividors(self):
        mn = min(self.num1,self.num2)
        common_dividors = []
        for i in range(1, mn+1):
            if self.num1 % i == 0 and self.num2 % i ==0:
                common_dividors.append(i)
        return common_dividors

x = Dividors(20, 10)
x.dividors()