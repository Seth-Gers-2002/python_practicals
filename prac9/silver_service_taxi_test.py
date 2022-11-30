from prac9.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
taxi.drive(18)
print(taxi)
print(taxi.get_fare())