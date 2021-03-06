# # Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# def print_funcs():
#     print(abs())
#     print(int())
#     print(input())
# # Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

# print_funcs()

#----------------------------------------------------
class Currency:
    def __init__(self,coin,amount):
        self.coin = coin
        self.amount = amount
    def __str__(self):
        return f'{self.amount} {self.coin}s'
    def __int__(self):
        return self.amount
    def __repr__(self):
        return f'{self.amount} {self.coin}s'
    def __add__(self,other):
        if self.coin == other.coin :
            return self.amount + other.amount
    def __iadd__(self,num):
        return f'{self.amount+num} {self.coin}s'

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(str(c1))
print(int(c1))
print(int(c1)+5)
print(c1.__add__(c2))
print(c1.__iadd__(5))
