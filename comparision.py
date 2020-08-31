import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
x=int(input())
y=int(input())
z=int(input())
if x>y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
elif z>x and z>y:
    print(z)