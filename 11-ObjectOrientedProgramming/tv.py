class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no = 1
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
      
   def show_status(self):
      if self.is_on == False:
         print('TV is off')
      elif self.is_on == True:
         print(f'TV is on, channel {self.channel_no}') 

   def set_channel(new_channel_no):
      new_channel_no = 5
      tv1 = TV()

      tv1.show_status()
      tv1.turn_on()
      tv1.show_status()
      tv1.channel_no = new_channel_no
      tv1.show_status()
      tv1.turn_off()
      tv1.show_status()




