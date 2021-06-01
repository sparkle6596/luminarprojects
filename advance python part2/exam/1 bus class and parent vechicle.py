class Vechicle:
    def details(self,category,model,colour):
        self.category=category
        self.model=model
        self.colour=colour
    def print(self):
        print(self.category,"\n",self.model,"\n",self.colour)

class Bus(Vechicle):
    def det(self,speed,system):
        self.speed=speed
        self.system=system
    def prints(self):
        print(self.speed,"\n",self.system)
pe=Vechicle()
pe.details("4wh",2001,"black")
pe.print()
st=Bus()
st.det(80,"automatic")
st.prints()
st.details("5wh",2012,"red")
st.print()