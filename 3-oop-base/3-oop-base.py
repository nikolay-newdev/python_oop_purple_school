from dataclasses import dataclass, field
from datetime import datetime, timedelta
import secrets


@dataclass
class Room:
    """Room Class"""
    id: int
    price: float
    #book_date: list = field(default_factory=list)


@dataclass
class SimpleRoom(Room):
    option: str = "Simple"


@dataclass
class LuxeRoom(Room):
    option: str = "Luxe"
    price_multiplier: float = 1.2

class Booking:
    def __init__(self, room: Room, check_in: datetime, check_out: datetime):
        self.id = "".join(secrets.choice("0123456789") for _ in range(6))
        self.room = room
        if datetime.strptime(check_in, "%d.%m.%Y") < datetime.strptime(check_out, "%d.%m.%Y"):
            self.check_in = datetime.strptime(check_in, "%d.%m.%Y")
            self.check_out = datetime.strptime(check_out, "%d.%m.%Y")
        else:
            raise ValueError("Дата отъезда должна быть позже даты въезда")
        self.is_active = True        
    
    def cancel(self):
        self.is_active = False
        return self

@dataclass
class Hotel: 
    """Hotel Class"""
    name: str
    rooms: list[SimpleRoom | LuxeRoom] = field(default_factory=list)
    bookings: list[Booking] = field(default_factory=list)
    
    def add_room(self, room: Room):
        self.rooms.append(room)
        return self.rooms

    def booking(self, room, check_in: datetime, check_out: datetime):
        """"Booking method"""
        b = Booking(room, check_in, check_out)
        if self.bookings:
            for booking in self.bookings:
                if booking.is_active:
                    if booking.room.id == b.room.id:
                        if (booking.check_in > b.check_out) or (booking.check_out < b.check_in):
                            self.bookings.append(b)
                            print(f"Бронирование #{b.id} подтверждено.")
                            return self
                        else:
                            raise ValueError(f"Room {room.id} is already booked from {booking.check_in} till {booking.check_out}. Try another dates.") 
            self.bookings.append(b)
            print(f"Бронирование #{b.id} подтверждено.")             
        else:
            self.bookings.append(b)
            print(f"Бронирование #{b.id} подтверждено.")
        return self

    def cancel(self, booking_id):
        for booking in self.bookings:
            if booking.id == booking_id:
                booking.cancel()
                print(f"Бронирование #{booking.id} отменено.")

    def show_booked(self):
        for booking in self.bookings:
            if booking.is_active:
                print(f"Бронь #{booking.id}, Номер {booking.room.id} забронирован с {datetime.strftime(booking.check_in, '%d.%m.%Y')} по {datetime.strftime(booking.check_out, '%d.%m.%Y')}")
        return self

    def show_available(self, check_in, check_out):
        check_in = datetime.strptime(check_in, "%d.%m.%Y")
        check_out = datetime.strptime(check_out, "%d.%m.%Y")
        set_dates = {check_in + timedelta(days=i) for i in range((check_out - check_in).days + 1)}
        available_rooms = []

        for room in self.rooms:
           set_booked_dates = [{booking.check_in + timedelta(days=i) for i in range((booking.check_out - booking.check_in).days + 1)} for booking in self.bookings  if booking.room.id == room.id and booking.is_active]
           if not any(set_dates & bd for bd in set_booked_dates):
               available_rooms.append(room)

        if available_rooms:
            print("Вот список свободных номеров:")
            for room in available_rooms:
                print(f"Номер #{room.id}, тип: {room.option}, стоимость за ночь: {room.price}")
        else:
            print("На выбранные даты нет доступных номеров")
                     
          
hotel = Hotel('Grand')
hotel.add_room(SimpleRoom(1, 100))
hotel.add_room(LuxeRoom(2, 120))
print(hotel.rooms)

hotel.booking(SimpleRoom(1, 100), '30.08.2026', '10.09.2026')
hotel.booking(LuxeRoom(2, 120), '30.08.2026', '10.09.2026')
hotel.booking(SimpleRoom(1, 100), '28.08.2026', '29.08.2026')

booking_number = hotel.bookings[0].id
hotel.cancel(booking_number)
hotel.booking(SimpleRoom(1, 100), '30.08.2026', '10.09.2026')

hotel.show_booked()
hotel.show_available('30.08.2026', '10.09.2026')
hotel.show_available('30.09.2026', '10.10.2026')

hotel.booking(LuxeRoom(2, 120), '30.08.2026', '10.09.2026')




