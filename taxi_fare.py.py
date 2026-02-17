"""
Taxi Fare Calculation
Base fare = $50
Distance fare = $10/km
"""

BASE_FARE = 50
PER_KM = 10


def calculate_fare(distance):
    return BASE_FARE + (PER_KM * distance)


# Example Run
if __name__ == "__main__":
    trips = [5, 10, 3]

    total = 0
    for i, d in enumerate(trips, start=1):
        fare = calculate_fare(d)
        total += fare
        print(f"Trip {i}: ${fare}")

    print(f"Total Fare: ${total}")
