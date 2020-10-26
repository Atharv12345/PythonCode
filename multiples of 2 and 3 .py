import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
x=input().split()
y=input().split()
x=[int(i) for i in x]
y=[int(i) for i in y]
for i in range(x[0],x[1]+1):
    if i%y[0]==0 and i%y[1]==0:
        print(i)
    # print(i,end=" ")