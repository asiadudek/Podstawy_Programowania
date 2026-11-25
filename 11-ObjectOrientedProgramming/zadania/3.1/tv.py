class TV:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
        

    def show_status(self):
        if self.is_on:
            print(f"TV is on")
        else:
            print(f"TV is off")
