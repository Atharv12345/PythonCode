import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
print("please enter the lenth and bredth ")
length=int(input())
breadth=int(input())
area=(length*breadth)
perimeter=2*(length+breadth)
print("Area =" ,area)
print("Perimeter=" ,perimeter)