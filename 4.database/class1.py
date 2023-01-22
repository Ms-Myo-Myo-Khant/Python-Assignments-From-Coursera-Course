class PartyAnimal:
    x=0
    def party(self):
        self.x=self.x+1
        print("So far",self.x)

an=PartyAnimal()

an.party()
an.party()#an is taking as parameter #object is taking as paramter
PartyAnimal.party(an)#same with an.party()
print(dir(an))
print(type(an))
p=PartyAnimal()
p.party()
