import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
x=input().split()
sum=0
for i in range(len(x)):
    x[i]=int(x[i])
    sum=sum+ x[i]
print(sum)