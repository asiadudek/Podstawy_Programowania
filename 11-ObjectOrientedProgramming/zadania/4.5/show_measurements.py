
from thermometer import Thermometer

def main():
    thermometer = Thermometer() #tworzymy nasz obiekt, termometr

    thermometer.turn_on()
    thermometer.measure() #mierzymy temperature
    thermometer.show_temperature()
    thermometer.turn_off()


if __name__ == "__main__":
    main()