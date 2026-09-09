import asyncio
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment
from datetime import datetime

async def main():
    # Inicializar sistemas
    reservation_system = ReservationSystem()
    customer_mgmt = CustomerManagement()
    room_mgmt = RoomManagement()

    # Crear habitaciones
    room_mgmt.add_room(Room(101,"Single", 100))
    room_mgmt.add_room(Room(103, "Double", 200))

    # Agregar clientes
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer_mgmt.add_customer(customer1)

    customer2 = Customer(2, "Robert", "robert@robert.com")
    customer_mgmt.add_customer(customer2)

    customer3 = Customer(3, "Carlos", "carlos@example.com")
    customer_mgmt.add_customer(customer3)

    alice_check_in = datetime(2026, 9, 10)
    alice_check_out = datetime(2026, 9, 15)

    robert_check_in = datetime(2026, 9, 20)
    robert_check_out = datetime(2026, 9, 25)

    
    # Verificar disponibilidad de habitaciones
    if reservation_system.check_room_availability(
        101,
        alice_check_in,
        alice_check_out
    ):
 
        payment_success = await process_payment("Alice", 100)

        if payment_success:
            reservation = Reservation(
                1,
                "Alice",
                101,
                alice_check_in,
                alice_check_out
            )

            reservation_system.add_reservation(reservation)

    carlos_check_in = datetime(2026, 9, 20)
    carlos_check_out = datetime(2026, 9, 25)

    if reservation_system.check_room_availability(
        101,
        carlos_check_in,
        carlos_check_out
    ): 
        payment_success = await process_payment("Carlos", 100)

        if payment_success:
            reservation = Reservation(
                3,
                "Carlos",
                101,
                carlos_check_in,
                carlos_check_out
            )   
            reservation_system.add_reservation(reservation)
      
    
    if reservation_system.check_room_availability(
        103,
        robert_check_in,
        robert_check_out
    ):
        payment_success = await process_payment("Robert", 200)
        if  payment_success:
            reservation = Reservation(
                2,
                "Robert",
                103,
                robert_check_in,
                robert_check_out
            )

            reservation_system.add_reservation(reservation)
  
   
if __name__ == "__main__":
    asyncio.run(main())

