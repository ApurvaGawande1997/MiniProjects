class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type  # e.g., Single, Double, Suite
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def release(self):
        if self.is_booked:
            self.is_booked = False
            return True
        return False

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room_number, room_type):
        room = Room(room_number, room_type)
        self.rooms.append(room)

    def list_available_rooms(self):
        return [room for room in self.rooms if not room.is_booked]

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.book()
        return False

    def release_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.release()
        return False

if __name__ == "__main__":
    my_hotel = Hotel("Sunset Inn")

    # Add rooms
    my_hotel.add_room(101, "Single")
    my_hotel.add_room(102, "Double")
    my_hotel.add_room(103, "Suite")

    # Book a room
    print("Booking 101:", my_hotel.book_room(101))  # True
    print("Booking 101 again:", my_hotel.book_room(101))  # False

    # List available rooms
    print("Available rooms:")
    for room in my_hotel.list_available_rooms():
        print(f"Room {room.room_number} ({room.room_type})")

    # Release a room
    print("Releasing 101:", my_hotel.release_room(101))  # True
