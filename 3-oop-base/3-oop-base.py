from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Room: 
    """Room Class"""
    id: int
    type: str
    price: float
    book_date: list = field(default_factory=list)
  


class Booking:        

    def booking(self, room_id, date_string):
        t = datetime.strptime(date_string, "%d.%m.%Y")
        return {"room_id": room_id, "time": t}
        
    def cancel_booking(self, room_id, date_string):
        t = datetime.strptime(date_string, "%d.%m.%Y")
        return {"room_id": room_id, "time": t}


@dataclass
class Hotel: 
    """Hotel Class"""
    name: str
    rooms: dict = field(default_factory=dict)
    
    def __post_init__(self):
        self.manage_room = Booking()


    def add_room(self, room: Room):
        self.rooms.update({room.id: room})
        return self.rooms

    def show_available_room(self, date_string):
        t = datetime.strptime(date_string, "%d.%m.%Y")
        for room in self.rooms.values():
            if t not in room.book_date:
                print(f"-Комната #{room.id}, тип: {room.type}, стоимость: {room.price}, доступна на {datetime.strftime(t, '%d.%m.%Y')}")
        return None

    def show_booked_room(self):
        print("Вот все забронированные номера и даты бронирования:")
        for room in self.rooms.values():
            if len(room.book_date) > 0:
                print(f"комната #{room.id} забронирована:")
                for d in room.book_date:
                    print(f"{datetime.strftime(d, '%d.%m.%Y')}")
        return None

    def booking(self, room_id, date_string):
        data = self.manage_room.booking(room_id, date_string)
        r = data["room_id"]
        t = data["time"]
        if r in self.rooms:
            current_room = self.rooms[r] 
            if t not in current_room.book_date:
                current_room.book_date.append(t)
                print(f"Номер #{current_room.id} успешно забронирован!")
            else:
                raise ValueError("Этот номер уже занят")
        else:
            raise ValueError("Такого номера не существует")

    def cancel_booking(self, room_id, date_string):
        data = self.manage_room.cancel_booking(room_id, date_string)
        r = data["room_id"]
        t = data["time"]
        if r in self.rooms:
            current_room = self.rooms[r]
            if t in current_room.book_date:
                current_room.book_date.remove(t)
                print(f"Бронирование номера #{current_room.id} отменено")
            else:
                raise ValueError(f"На эту дату нет бронирования номера # {current_room.id}")
        else:
            raise ValueError("Такого номера не существует")
        


hotel = Hotel('Grand')
hotel.add_room(Room(1, 'Small', 100))
hotel.add_room(Room(2, 'Small', 100))
hotel.add_room(Room(3, 'Luxe', 200))


hotel.booking(1, '29.08.2026')

hotel.cancel_booking(1, '29.08.2026')

hotel.show_available_room('29.08.2026')

hotel.booking(1, '29.08.2026')
hotel.booking(1, '30.08.2026')
hotel.show_booked_room()