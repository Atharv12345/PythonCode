import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
x=input().split("_")
for i in  range (len(x)):
    x[i]=x[i].title()
    print(x[i],end="")
    