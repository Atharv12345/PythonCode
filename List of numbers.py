import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
x=input().split()
#print(x)
a=len(x)
#print(a)
sum=0
for i in range(a):
    sum=(sum+int(x[i]))
print(sum)