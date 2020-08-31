import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
x=int(input())
for i in range(10):
    print(x*(i+1))