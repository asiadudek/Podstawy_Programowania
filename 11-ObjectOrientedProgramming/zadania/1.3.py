class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km #stawka za 1km
        self.distance = 0
        self.fare = 0 #oplata za przejazd

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print("RECEIPT")
        print()
        print(f'Distance: {self.distance} km')
        print(f'Fare: {self.fare} €')
        print(f'Rate per km: {self.rate_per_km} eur/km')


def main():
    ride1 = TaxiRide(2) #czyli 2 euro za km
    ride2 = TaxiRide(3)

    ride1.calculate_fare(10) #oplata za 10 km
    ride2.calculate_fare(5)

    ride1.print_receipt()
    print()
    ride2.print_receipt()
   

if __name__ == "__main__":
    main()
