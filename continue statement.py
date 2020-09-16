import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
x=input().split()
#print(x)
a=len(x)
#print(a)
for i in range(a):
    if x[i]=="Alia":
        continue
    print("Hello",x[i])
    