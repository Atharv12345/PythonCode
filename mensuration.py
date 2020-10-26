class mensuration:
    def __init__(self,radius):
        self.radius=radius
        self.pi=3.14
    def area_of_circle(self):
        area=self.pi*self.radius**2
        return area
    def perimeter_of_circle(self):
        perimeter=self.radius*self.pi*2
        return perimeter
    def volume_of_sphere(self):
        volume=4/3*self.pi*self.radius**3
        return volume
if __name__=="__main__":
    print("Please enter the radius")
    a=int(input())
    s=mensuration(a)

    print("What do you want to know \n1.Area\n2.Perimeter\n3.Volume")
    b=int(input())
    if b==1:
        print("Area:",s.area_of_circle())
    elif b==2:
        print("Perimeter:",s.perimeter_of_circle())
    elif b==3:
        print("Volume:",s.volume_of_sphere())


        