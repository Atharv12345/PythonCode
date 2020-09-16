import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
x=int(input())
y=(input())
z="*"
z=z*x
print(z+y+z)