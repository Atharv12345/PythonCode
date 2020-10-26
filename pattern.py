import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
rows=int(input())
columns=int(input())
a=input()
for i in range(rows):
    for j in range(columns):
        print(a,end=" ")
    print()