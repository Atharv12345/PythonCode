import sysb
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
x=int(input())
x=abs(x)
sumofdigits=0
while x>0:
    sumofdigits=x%10+sumofdigits
    x=x//10
    print(x,sumofdigits)
print (sumofdigits)