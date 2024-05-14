class Passenger:
    def __init__(self,flights):
        self.flights = flights
        while True:
            print("\nWelcome to the Passenger Page")
            print("1. Book Flights")
            print("2. Display Flights")
            print("3. Exit")

            try:
                c = input('Enter your choice:')
                if c == "1":
                    self.flights.book_flights();
                elif c == "2":
                    self.flights.display_flight();
                elif c == "3":
                    print('Thank you! GoodBye...')
                    break
                else:
                    print('Invalid value!')
            except Exception as err:
                print(err)