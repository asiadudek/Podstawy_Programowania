class Phone:
    def __init__(self, brand):
        self.brand = brand
        self.battery = 50
        self.is_on = False
        self.volume = 3

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} is now on")

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"Battery charged to: {self.battery}%")

    def change_volume(self, new_volume):
        self.volume += new_volume
        print(f"Volume set to: {self.volume}")

    def display_info(self):
        print("PHONE INFO")
        print(f"Brand: {self.brand}")
        print(f"Battery: {self.battery}%")
        print(f"Is on: {self.is_on}")
        print(f"Volume: {self.volume}")

def main():
    my_phone = Phone("Samsung")

    my_phone.turn_on()
    my_phone.charge(40)
    my_phone.change_volume(5)

    my_phone.display_info

if __name__ == '__main__':
    main()

