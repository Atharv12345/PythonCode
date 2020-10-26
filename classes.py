import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
class Student:
    def __init__(self,aadhar,age):
        self.aadhar=aadhar
        self.age=age
    def vote_eligibility(self):
        if self.age >18 and self.aadhar=='yes':
            print("Student is eligible to vote")
        elif self.age>18 and self.aadhar=='no':
            print("You need an aadhaar card to vote")
        else:
            print("Student is not eligible to vote")
if __name__=="__main__":
    # Atharv=Student('no',19)
    # print(Atharv.vote_eligibility())
    a=input()
    b=int(input())
    Atharv=Student(a,b)
    Atharv.vote_eligibility()