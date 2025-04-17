from dao.VehicleDAOImpl import VehicleDAOImpl
from dao.RouteDAOImpl import RouteDAOImpl
from dao.TripDAOImpl import TripDAOImpl
from dao.PassengerDAOImpl import PassengerDAOImpl
from dao.BookingDAOImpl import BookingDAOImpl

from entity.Vehicle import Vehicle
from entity.Route import Route
from entity.Trip import Trip
from entity.Passenger import Passenger
from entity.Booking import Booking

from exception.VehicleNotFoundException import VehicleNotFoundException
from exception.BookingNotFoundException import BookingNotFoundException
from exception.PassengerNotFoundException import PassengerNotFoundException
from exception.TripNotFoundException import TripNotFoundException

from util.DBConnect import db_connection
from datetime import datetime
import traceback


def menu():
    vehicle_dao = VehicleDAOImpl()
    route_dao = RouteDAOImpl()
    trip_dao = TripDAOImpl()
    passenger_dao = PassengerDAOImpl()
    booking_dao = BookingDAOImpl()

    while True:
        print("\n========== Transport Management System ==========")
        print("1. Add Vehicle")
        print("2. Update Vehicle")
        print("3. Delete Vehicle")
        print("4. Schedule Trip")
        print("5. Cancel Trip")
        print("6. Book Trip")
        print("7. Cancel Booking")
        print("8. Get Bookings by Passenger")
        print("9. Get Bookings by Trip")
        print("10. Add Route")
        print("11. Add Passenger")
        print("12. List All Vehicles")
        print("13. List All Trips")
        print("14. List All Routes")
        print("15. List All Passengers")
        print("16. List Table Names")
        print("0. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                model = input("Model: ")
                cap = float(input("Capacity: "))
                vtype = input("Type (Truck/Van/Bus): ")
                status = input("Status (Available/On Trip/Maintenance): ")
                vehicle = Vehicle(model=model, capacity=cap, v_type=vtype, status=status)
                vehicle_dao.insert_vehicle(vehicle)
                print("Vehicle added.")

            elif choice == '2':
                vid = int(input("Vehicle ID: "))
                model = input("New Model: ")
                cap = float(input("New Capacity: "))
                vtype = input("New Type (Truck/Van/Bus): ")
                status = input("New Status (Available/On Trip/Maintenance): ")
                vehicle = Vehicle(vehicle_id=vid, model=model, capacity=cap, v_type=vtype, status=status)
                vehicle_dao.update_vehicle(vehicle)
                print("Vehicle updated.")

            elif choice == '3':
                vid = int(input("Vehicle ID to delete: "))
                vehicle_dao.delete_vehicle(vid)
                print("Vehicle deleted.")

            elif choice == '4':
                vehicle_id = int(input("Vehicle ID: "))
                route_id = int(input("Route ID: "))
                dep_date = input("Departure (YYYY-MM-DD HH:MM): ")
                arr_date = input("Arrival (YYYY-MM-DD HH:MM): ")
                status = "Scheduled"
                trip_type = input("Trip Type (Freight/Passenger): ")
                max_passengers = int(input("Max Passengers: "))
                trip = Trip(vehicle=Vehicle(vehicle_id=vehicle_id),
                            route=Route(route_id=route_id),
                            departure_date=dep_date,
                            arrival_date=arr_date,
                            status=status,
                            trip_type=trip_type,
                            max_passengers=max_passengers)
                trip_dao.schedule_trip(trip)
                print("Trip scheduled.")

            elif choice == '5':
                trip_id = int(input("Trip ID to cancel: "))
                trip_dao.cancel_trip(trip_id)
                print("Trip cancelled.")

            elif choice == '6':
                trip_id = int(input("Trip ID: "))
                passenger_id = int(input("Passenger ID: "))
                booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                booking = Booking(trip=Trip(trip_id=trip_id),
                                  passenger=Passenger(passenger_id=passenger_id),
                                  booking_date=booking_date,
                                  status="Confirmed")
                booking_dao.insert_booking(booking)
                print("Booking confirmed.")

            elif choice == '7':
                booking_id = int(input("Booking ID to cancel: "))
                booking_dao.cancel_booking(booking_id)
                print("Booking cancelled.")

            elif choice == '8':
                pid = int(input("Passenger ID: "))
                bookings = booking_dao.get_bookings_by_passenger(pid)
                if bookings:
                    for b in bookings:
                        print(b)
                else:
                    print("No bookings found for this passenger.")

            elif choice == '9':
                tid = int(input("Trip ID: "))
                bookings = booking_dao.get_bookings_by_trip(tid)
                if bookings:
                    for b in bookings:
                        print(b)
                else:
                    print("No bookings found for this trip.")

            elif choice == '10':
                start = input("Start Destination: ")
                end = input("End Destination: ")
                distance = float(input("Distance: "))
                route = Route(start_destination=start, end_destination=end, distance=distance)
                route_dao.insert_route(route)
                print("Route added.")

            elif choice == '11':
                name = input("First Name: ")
                gender = input("Gender: ")
                age = int(input("Age: "))
                email = input("Email: ")
                phone = input("Phone Number: ")
                passenger = Passenger(first_name=name, gender=gender, age=age, email=email, phone_number=phone)
                passenger_dao.insert_passenger(passenger)
                print("Passenger added.")

            elif choice == '12':
                vehicles = vehicle_dao.get_all_vehicles()
                for v in vehicles:
                    print(v)

            elif choice == '13':
                trips = trip_dao.get_all_trips()
                for t in trips:
                    print(t)

            elif choice == '14':
                routes = route_dao.get_all_routes()
                for r in routes:
                    print(r)

            elif choice == '15':
                passengers = passenger_dao.get_all_passengers()
                for p in passengers:
                    print(p)

            elif choice == '16':
                print("\nList of Tables in the Transport Management System:")
                print("1. Vehicles")
                print("2. Routes")
                print("3. Trips")
                print("4. Passengers")
                print("5. Bookings")

            elif choice == '0':
                print("Thank you for using Transport Management System.")
                break

            else:
                print("Invalid choice. Please try again.")

        except VehicleNotFoundException as ve:
            print("VehicleNotFoundException occurred:")
            traceback.print_exc()
        except BookingNotFoundException as be:
            print("BookingNotFoundException occurred:")
            traceback.print_exc()
        except PassengerNotFoundException as pe:
            print("PassengerNotFoundException occurred:")
            traceback.print_exc()
        except TripNotFoundException as te:
            print("TripNotFoundException occurred:")
            traceback.print_exc()
        except Exception as e:
            print("An unexpected error occurred:")
            traceback.print_exc()


if __name__ == "__main__":
    menu()
