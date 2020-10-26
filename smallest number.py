import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
y=input().split()
y=[int(i) for i in (y)]
smallest_number=y[0]
for i in range(len(y)):
    if smallest_number>y[i]:
        smallest_number=y[i]
print(smallest_number)