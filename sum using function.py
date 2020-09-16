import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def sum(a,b,c):
    return a+b+c
a=int(input())
b=int(input())
c=int(input())
d=sum(a,b,c)
print ("Sum =",d)