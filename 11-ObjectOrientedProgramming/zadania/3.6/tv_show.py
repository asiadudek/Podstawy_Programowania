from tv import TV



def main():
   my_tv = TV()
   my_tv.show_status()
   my_tv.turn_on()
   my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
   my_tv.show_status()
   my_tv.set_channel(4)
   my_tv.show_status()

   my_tv.volume_up()
   my_tv.volume_up()
   my_tv.show_status()

   my_tv.volume_down()
   my_tv.show_status()

   my_tv.turn_off()
   my_tv.show_status()


if __name__ == "__main__":
   main() 


