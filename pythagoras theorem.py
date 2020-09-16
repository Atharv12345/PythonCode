import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
x=input().split()
def pythagoras(a,b,c):
    m=a**2+b**2
    n=c**2
    if m==n:
        print("This is a right Triangle")
    else:
        print("This is not a right triangle")
# print(x)
for i in range(len(x)):
    x[i]=int(x[i])
# print(x)
pythagoras(x[0],x[1],x[2])