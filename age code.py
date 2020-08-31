import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
print("Please enter your age to check if you are eligable to vote")
y=int(input())
if 18>y:
    print("You are not eligible to vote")
elif 18<y:
    print("You are eligible to vote")
