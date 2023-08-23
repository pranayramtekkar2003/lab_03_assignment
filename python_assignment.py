class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def search_by_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None
    
    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
        return result
    
    def search_by_destination(self, destination):
        result = []
        for flight in self.flights:
            if flight.destination == destination:
                result.append(flight)
        return result

def main():
    flight_table = FlightTable()
    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    while True:
        print("Select search type:")
        print("1. Flight ID")
        print("2. Source City")
        print("3. Destination City")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            flight_id = input("Enter Flight ID: ")
            flight = flight_table.search_by_id(flight_id)
            if flight:
                print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
            else:
                print("Flight not found.")
        elif choice == 2:
            source = input("Enter Source City: ")
            flights = flight_table.search_by_source(source)
            if flights:
                for flight in flights:
                    print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
            else:
                print("No flights found for the given source.")
        elif choice == 3:
            destination = input("Enter Destination City: ")
            flights = flight_table.search_by_destination(destination)
            if flights:
                for flight in flights:
                    print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
            else:
                print("No flights found for the given destination.")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()