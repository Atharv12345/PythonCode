import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=int(input())
n=input()
for i in range(a,0,-1):
    for m in range(i):
        print(n,end=" ")
    print()