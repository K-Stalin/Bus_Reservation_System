class Bus():
    def __init__(self,bus_no,ac,capacity,bus_route):
        self.bus_no = bus_no
        self.ac = ac
        self.capacity = capacity
        self.bus_route= bus_route
    
    def to_dict(self):
        return {
             "bus_no":self.bus_no,
             "ac":self.ac,
             "capacity":self.capacity,
             "bus_route":self.bus_route
        }       


class Reservation():
    def __init__(self,passanger_name,bus_no,travel_date):
        self.passanger_name = passanger_name
        self.bus_no = bus_no
        self.travel_date = travel_date
        
    def to_dict(self):
        return {
             "passamger_name":self.passanger_name,
             "bus_no":self.bus_no,
             "travel_date":self.travel_date
        }
        



class reservation_system():
    
    def __init__(self):
        self.Buses   = []
        self.Bookings = []
            
    def add_buses(self,bus):
        self.Buses.append(bus)
                
    def view_buses(self):
        for bus in self.Buses:
            print(bus.to_dict())
        print("-"*40)
            
    def make_reservation(self,passanger_name,bus_no,travel_date):
        booked_seats =0
        for x  in self.Buses:
            if x.bus_no == bus_no:
                print("Bus found")
                for  booking in self.Bookings:
                    if booking.bus_no ==  bus_no and booking.travel_date == travel_date:
                        booked_seats+=1
                if booked_seats < x.capacity:
                    reserve = Reservation(passanger_name,bus_no,travel_date)
                    self.Bookings.append(reserve)
                    print("Reservation Successful! Happy journey!🚍")
                    print("-"*40)
                else:
                    print("No seats avilable.Reservation failed❗") 
        if x.bus_no != bus_no:
            print("User Entered BusNO and Available BusNo are not Match!")
         
    def view_reservation(self):
        for  reserve in self.Bookings:
            print(reserve.to_dict())
        print("-"*40)

bus1 = Bus("TN50","Yes",10,"Chennai To Mannargudi")
bus2 = Bus("TN20","NO",2,"Shenkottai To Thanjavur")
reservation = reservation_system()
reservation.add_buses(bus1)
reservation.add_buses(bus2)


while True:
    print("Bus Reservation Menu:")
    print("1.Booking")
    print("2.View Booking")
    print("3.view Buses")
    print("4.Exit")
    user_option = input("Enter  your choice (1-4): ")
    print("-"*40)
    if user_option == "1":
        reservation.make_reservation(input("Enter your Name: "),input("Enter your BusNo: "),input("Enter your Travel Date: "))
    elif user_option == "2":
        reservation.view_reservation()
    elif user_option == "3":
        reservation.view_buses()
    elif user_option == "4":
        print("Exiting... GoodBye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")
                   

