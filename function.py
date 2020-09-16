import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def area(a,b):
    return a*b
def perimeter(a,b):
    return 2*(a+b)
length=int(input())
breadth=int(input())
c=area(length,breadth)
d=perimeter (length,breadth)
print("Area = ",c)
print("Perimeter=",d)