import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
number_of_rows=int(input())
a=[]
for i in range(number_of_rows):
    a.append(input().split())
print(a)