import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
x=input().split()
x=[int(i) for i in (x)]
largest_number=x[0]
for i in range(len(x)):
    if largest_number<x[i]:
        largest_number=x[i]
print(largest_number)