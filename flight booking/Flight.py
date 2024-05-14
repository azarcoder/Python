class Flight:
    def __init__(self):
        self.flights_list = []
        while True:
            print("\nWelcome to the Flight Page")
            print("1. Display Flights")
            print("2. Add Flights")
            print("3. Exit")

            try:
                c = input('Enter your choice:')
                if c == "1":
                    self.display_flight()

                elif c == "2":
                    self.add_flight()

                elif c=="3":
                    print("Goodbye!")
                    break
                else:
                    print('Invalid value!')
            except Exception as err:
                print(err)
    
    def display_flight(self):
        if len(self.flights_list) > 0:
            print("Displaying Flights:")
            for flight in self.flights_list:
                print(flight)
        else:
            print('No filghts found!')
    
    def add_flight(self):
        flight_number = input("Enter flight number: ")
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        departure_time = input("Enter departure time: ")
        arrival_time = input("Enter arrival time: ")
        price = float(input("Enter price: "))
        capacity = int(input("Enter capacity: "))
        new_flight = {
            "flight_number": flight_number,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "price": price,
            "capacity": capacity,
            "seats_booked" : 0,
        }
        self.flights_list.append(new_flight)
        print('Added Succesfully!')
    

    def find_flight_by_number(self, choice):
        for flight in self.flights_list:
            if flight['flight_number'] == choice:
                return flight
        return None

    def book_flights(self):
        print('\n***** Book Flights ******')
        print('Flights list:')
        self.display_flight()
        choice = input("Enter the flight number you want to book: ")
        flight = self.find_flight_by_number(choice)
        print(flight)
        if flight:
            num_tickets = int(input("Enter the number of tickets you want to book: "))
            if flight['capacity'] - flight['seats_booked'] >= num_tickets:
                flight['seats_booked'] += num_tickets
                print(f"{num_tickets} ticket(s) booked successfully for flight {flight['flight_number']}.")
                print(f"Remaining seats: {flight['capacity'] - flight['seats_booked']}")
            else:
                print("Sorry, not enough seats available.")
                return
        else:
            print('Invalid flight number!')


        


