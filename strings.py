import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=input()
b=len(a)
print (a[0]+a[-1])
print(b,"character")