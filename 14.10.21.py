class Point():
    x=0
    y=0
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def set_cordinates(self,x,y):
        self.x=x
        self.y=y
    def get_distance(self,p2):
        try:
         print(((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5)
        except:
            print('Передана не точка')




p1=Point()
p2=Point()
p1.set_cordinates(1,2)
p2.set_cordinates(4,6)
d=p1.get_distance(p2)