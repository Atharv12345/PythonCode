import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
n=int(input())
a=input()
for i in range(n):
    for k in range(n-i-1):
        # print(" ",end="")
        print(end=" ")
    for j in range(i+1):
        print(a,end=" ")
    print()