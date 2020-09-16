import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def sum(a,b,c):
    sum=0
    if a%2==0:
        sum=sum+a
    if b%2==0:
        sum=sum+b
    if c%2==0:
        sum=sum+c
    return sum 
print("Please enter 3 numbers in different lines")
a=int(input())
b=int(input())
c=int(input())
d=sum(a,b,c)
print("Sum:",d)
