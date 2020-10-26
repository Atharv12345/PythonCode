import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=input()
temperature=a[:-1]
character=a[-1]
temperature=float(temperature)
# print(b,c)
# print(type(a),type(b))
if character=='C':
    print(temperature,character)
    f=9/5*temperature+32
    print(f,'F')
    k=temperature+273.15
    print(k,'K')
elif character=='F':
    c=(temperature-32)*5/9
    print(c,'C')
    print(temperature,'F')
    k=c+273.15
    print(k,'K')
elif character=='K':
    c=(temperature-273.15)
    print(c,'C')
    f=9/5*c+32
    print(f,'F')
    print(temperature,'K')