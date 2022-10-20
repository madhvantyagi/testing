
class box:
    def __init__(self,name,age):
        self.word=name
        self.experience=age

    def show_var(self):
        for x in range(20):
             print(self.word,self.experience) 

                  





class Table(box):
    def __init__(self,name,experience):
        super().__init__(name,experience) 
        b=box(name,experience)
        b.show_var()

     



t=Table("madhavan",34134)
