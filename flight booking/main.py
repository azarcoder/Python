import Flight as fg
import Passenger as pg

def main():
    while True:
        print("\nWelcome to the Flight Booking System")
        print("1. Flight")
        print("2. Passenger")
        print("3. Exit")

        try:
            c = input('Enter your choice:')
            if c == "1":
                flights = fg.Flight()
            elif c == "2":
                passengers = pg.Passenger(flights)
            elif c=="3":
                print("Thank you for using the Flight Booking System. Goodbye!")
                break
            else:
                print('Invalid value!')
        except Exception as err:
            print(err)

if __name__ == "__main__":
    main()
