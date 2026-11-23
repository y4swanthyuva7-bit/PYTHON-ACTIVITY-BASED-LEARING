from datetime import datetime
import math

# Parking rates per hour
RATES = {
    "two-wheeler": 10,
    "car": 20,
    "bus": 30
}

# Maximum daily parking charges
DAILY_LIMITS = {
    "two-wheeler": 100,
    "car": 200,
    "bus": 300
}

PENALTY = 200
PENALTY_HOURS = 72


def calculate_parking_fee():

    print("===================================")
    print(" SMART PARKING FEE MANAGEMENT")
    print("===================================")

    # Vehicle details
    vehicle_number = input("Enter Vehicle Number: ")

    print("\nVehicle Categories:")
    print("1. Two-wheeler")
    print("2. Car")
    print("3. Bus")

    choice = input("Select Vehicle Category (1-3): ")

    categories = {
        "1": "two-wheeler",
        "2": "car",
        "3": "bus"
    }

    if choice not in categories:
        print("Invalid vehicle category!")
        return

    vehicle_type = categories[choice]

    # Get entry and exit time
    time_format = "%Y-%m-%d %H:%M"

    try:
        entry_time = datetime.strptime(
            input("Enter Entry Date and Time (YYYY-MM-DD HH:MM): "),
            time_format
        )

        exit_time = datetime.strptime(
            input("Enter Exit Date and Time (YYYY-MM-DD HH:MM): "),
            time_format
        )

    except ValueError:
        print("Invalid date or time format!")
        return

    # Validate time
    if exit_time <= entry_time:
        print("Error: Exit time must be after entry time!")
        return

    # Calculate parking duration
    duration = (exit_time - entry_time).total_seconds() / 3600

    # Round up partial hours
    total_hours = math.ceil(duration)

    # Calculate parking fee
    hourly_rate = RATES[vehicle_type]
    daily_limit = DAILY_LIMITS[vehicle_type]

    # Calculate charges for each 24-hour period
    days = total_hours // 24
    remaining_hours = total_hours % 24

    parking_fee = (days * daily_limit) + min(
        remaining_hours * hourly_rate,
        daily_limit
    )

    # Overnight parking check
    overnight = entry_time.date() != exit_time.date()

    # Penalty calculation
    penalty = 0

    if duration > PENALTY_HOURS:
        penalty = PENALTY

    # Final fee
    total_fee = parking_fee + penalty

    # Display receipt
    print("\n========== PARKING RECEIPT ==========")
    print("Vehicle Number :", vehicle_number)
    print("Vehicle Type   :", vehicle_type)
    print("Entry Time     :", entry_time)
    print("Exit Time      :", exit_time)
    print("Parking Hours  :", round(duration, 2))
    print("Charged Hours  :", total_hours)
    print("Overnight      :", "Yes" if overnight else "No")
    print("Parking Fee    : Rs.", parking_fee)
    print("Penalty        : Rs.", penalty)
    print("------------------------------------")
    print("TOTAL FEE      : Rs.", total_fee)
    print("====================================")
