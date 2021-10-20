#class Zebra:

  #  def which_stripe(self):
   #  stripe = {1:'полоска белая',2: 'полоска черная'}

 #   for key in stripe:
  #       print(key)



#z1=Zebra()
#z1.which_stripe()


class Zebra:
    counter = 0
    def which_stripe(self):
        if self.counter % 2 == 0:
            print("Полоска белая")
            Zebra.counter += 1
        else:
            print("Полоска черная")
            Zebra.counter += 1

z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe()
