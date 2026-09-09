class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.available = True

class RoomManagement:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        """Agrega una nueva habitación al sistema."""
        self.rooms[room.room_number] = room
        print(f"Habitación {room.room_number} agregada")

    def check_availability(self, room_number):
        """Verifica si una habitación está disponible."""
        room = self.rooms.get(room_number)
        if room and room.available:
            print(f"Habitacion {room_number} esta disponible")
            return True
        print(f"Habitación {room_number} no esta disponible")
        return False

    def reserve_room(self, room_number):
        room = self.rooms.get(room_number)

        if room:
            room.available = False
            print(f"Habitación {room_number} reservada")
        else:
            print(f"Habitación {room_number} no encontrada")

    def release_room(self, room_number):
        room = self.rooms.get(room_number)

        if room:
            room.available = True
            print(f"Habitación {room_number} liberada")
        else:
            print(f"Habitación {room_number} no encontrada")