
class car:
    def __init__(self,color,brand,wheels,model):
        self.color=color
        self.brand=brand
        self.wheels=wheels
        self.model=model

    def display(self):
        print(self.color)
        print(self.brand)
        print(self.wheels)
        print(self.model)

# t1=car("white","TATA",4,"NANO")
# t1.display()

t2=car("black","Hyundai",4,"Santro")
t2.display()