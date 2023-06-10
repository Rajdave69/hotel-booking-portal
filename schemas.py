class HotelRoom:
    def __init__(self, number, capacity, price):
        self.number = number
        self.capacity = capacity
        self.price = price
        self.type = None
        self.availability = None
        # Rooms can be booked 30 days in advance
        # self.availability is a list of 30 booleans corresponding to the next 30 days

    def is_available(self):
        pass

    def book(self):
        pass

    def price_for(self, nights):
        pass

    def __repr__(self):
        return f"HotelRoom(number={self.number}, capacity={self.capacity}, price={self.price})"


class SingleRoom(HotelRoom):
    def __init__(self, number, price):
        super().__init__(number, 1, price)
        self.type = "Single"


class DoubleRoom(HotelRoom):
    def __init__(self, number, price):
        super().__init__(number, 2, price)
        self.type = "Double"


class TripleRoom(HotelRoom):
    def __init__(self, number, price):
        super().__init__(number, 3, price)
        self.type = "Triple"


class FamilyRoom(HotelRoom):
    def __init__(self, number, price):
        super().__init__(number, 4, price)
        self.type = "Family"


class Hotel:
    def __init__(self, name, rating, rooms: list[HotelRoom]):
        self.name = name
        self.rating = rating
        self.rooms = rooms

    def book(self, room_number):
        pass

    def cancel(self, room_number):
        pass

    def __repr__(self):
        return f"Hotel(name={self.name}, rating={self.rating}, rooms={self.rooms})"
