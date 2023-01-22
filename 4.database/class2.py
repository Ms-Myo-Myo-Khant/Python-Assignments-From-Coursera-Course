class PartyAnimal:
    x=0
    def __init__(self,z):#constructor
        self.name=z
        print(self.name,"constructed\n")

    def __del__(self):#destructor
        print(self.name,'destructed\n')

    def party(self):
        self.x=self.x+1
        print(self.name,' party count ',self.x)

an=PartyAnimal('Sally')

an.party()



p=PartyAnimal('Jim')
p.party()
an.party()
an=42
print("an is reassign with integer value :",an)
