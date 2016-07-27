class Cars():


  # def carMods(self):
  #   with open("car-models.txt", 'w') as mods : #with closes file automatically after looping
  #     mods.write('M3, Elise, 911')


  def carModels(self):
    mod = []
    with open("car-models.txt", 'w') as models: #with closes file automatically after looping
      models.write('M3, Elise, 911')

    with open("car-models.txt", 'r') as models:
      models = models.read()
      models = models.split(",")
      for m in models:
        mod.append(m)
    return mod



  def carMakes(self):
    make = []
    with open("car-makes.txt", 'r') as makes : #with closes file automatically after looping
      for m in makes:
        make.append(m[:-1])
    return(make)


  def genDict(self):
    modlist = []
    mods = self.carModels()
    for m in mods:
      modlist.append([m])



    makes = self.carMakes()


    carDict = dict(zip(makes, modlist))
    print (carDict)













if __name__ == '__main__':
  car = Cars()
  car.genDict()
