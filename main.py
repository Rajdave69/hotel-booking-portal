from schemas import *

cls = lambda: print('\n' * 100)
cls()


class Frontend:
    def __init__(self):
        rooms = []

        # Create the rooms
        rooms.extend(SingleRoom(i, 100) for i in range(0, 10))
        rooms.extend(DoubleRoom(i, 200) for i in range(10, 20)),
        rooms.extend(TripleRoom(i, 300) for i in range(20, 30)),
        rooms.extend(FamilyRoom(i, 400) for i in range(30, 40))

        self.hotel = Hotel("Hotel California", 5, rooms)
        self.my_bookings = []

        while True:
            self.run()

    def run(self):
        print(" ")
        print(" ")
        print("---------------------------------------")
        print("Welcome to the Hotel Booking Platform")
        print(f"Serving Hotel {self.hotel.name}")
        print(f"{self.hotel.rating} stars")
        print(" ")
        print("Please select an option:")
        print("1. Book a room")
        print("2. Cancel a booking")
        print("3. Show my bookings")
        print("3. Exit")

        option = input("Option: ")

        try:
            option = int(option)
            if option not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Invalid option selected. Must be 1, 2 or 3")
            return self.run()

        if option == 1:
            self.book()

        elif option == 2:
            self.cancel_booking()

        elif option == 3:
            self.show_bookings()

    def select_room(self):
        cls()
        print("Please select a room type:")
        print("1. Single")
        print("2. Double")
        print("3. Triple")
        print("4. Family")

        option = input("Option: ")

        try:
            option = int(option)
            if option not in [1, 2, 3, 4]:
                raise ValueError
        except ValueError:
            print("Invalid option selected. Must be 1, 2, 3 or 4")
            return self.select_room()

        if option == 1:
            return SingleRoom
        elif option == 2:
            return DoubleRoom
        elif option == 3:
            return TripleRoom
        elif option == 4:
            return FamilyRoom

        else:
            return option

    def book(self):
        cls()
        print(f"Booking a room at {self.hotel.name}")
        room_type = self.select_room()

        # Filter the rooms by type
        available_rooms = list(filter(lambda room: isinstance(room, room_type), self.hotel.rooms))

        if len(available_rooms) == 0:
            print("No rooms of this type are available")
            return self.run()

        print(" ")

        # Print the available rooms
        print("The following rooms are available with their prices:")
        for room in available_rooms:
            print(room.number, room.price)

        print(" ")

        # Select a room
        room_number = input("Please select a room number: ")

        try:
            room_number = int(room_number)
        except ValueError:
            print("Invalid room number entered")
            return self.run()

        if room_number not in [available_rooms[i].number for i in range(len(available_rooms))]:
            print("Invalid room number entered")
            return self.run()

        room = self.hotel.rooms[room_number]

        # Book the room
        self.hotel.book(room_number)
        print("Room booked successfully")
        print(f"Your room number is {room_number}")
        print(f"You must pay {room.price}")
        print("Thank you for booking with us")

        self.my_bookings.append(room)

        return self.run()

    def cancel_booking(self):
        cls()
        if not self.my_bookings:
            print("You have no bookings")
            return self.run()

        print(" ")

        print("The following are your bookings:")
        for booking in self.my_bookings:
            print(booking.number, booking.price)

        print(" ")

        room_number = input("Please select a room number to cancel: ")

        try:
            room_number = int(room_number)
        except ValueError:
            print("Invalid room number entered")
            return self.run()

        if room_number not in self.my_bookings:
            print("Invalid room number entered")
            return self.run()

        self.hotel.cancel(room_number)
        print("Room cancelled successfully")

        self.my_bookings.remove(room_number)

        return self.run()

    def show_bookings(self):
        cls()
        if not self.my_bookings:
            print("You have no bookings")
            return self.run()

        print(" ")

        print("The following are your bookings:")
        print("Room Number | Price | Type")
        for booking in self.my_bookings:
            print(f"#{booking.number} | {booking.price} | {booking.type}")

        return self.run()


Frontend()
