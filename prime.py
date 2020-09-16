import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
x=int(input())
if x==1:
    print("The number is neither prime nor composite")
    # exit()
p=0
for i in range(2,x//2+1):
    if x%i==0:
        p=1        
        break
if p==1:
    print("The number is not a prime number.")
elif p==0:
    print("The number is a prime number")
 