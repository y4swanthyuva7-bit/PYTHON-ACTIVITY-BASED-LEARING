# Progressive Water Tariff Analysis System

# Tariff rates
RATE_1 = 5       # 0-10 KL
RATE_2 = 10      # 11-20 KL
RATE_3 = 15      # Above 20 KL

FIXED_FEE = 50
EXCESS_LIMIT = 25
PENALTY = 100


# Function to calculate water bill
def calculate_bill(consumption):

    bill = 0

    # First slab: 0 to 10 KL
    if consumption <= 10:
        bill = consumption * RATE_1

    # Second slab: 11 to 20 KL
    elif consumption <= 20:
        bill = (10 * RATE_1) + (
            (consumption - 10) * RATE_2
        )

    # Third slab: Above 20 KL
    else:
        bill = (10 * RATE_1) + (
            10 * RATE_2
        ) + (
            (consumption - 20) * RATE_3
        )

    # Add fixed monthly fee
    bill += FIXED_FEE

    # Apply excessive usage penalty
    penalty = 0

    if consumption > EXCESS_LIMIT:
        penalty = PENALTY

    total_bill = bill + penalty

    return bill - FIXED_FEE, penalty, total_bill


# Main program
def water_tariff_analysis():

    print("======================================")
    print(" PROGRESSIVE WATER TARIFF ANALYSIS")
    print("======================================")

    try:
        n = int(input("Enter number of households: "))

        if n <= 0:
            print("Number of households must be positive!")
            return

        households = []

        # Collect household details
        for i in range(n):

            print("\nHousehold", i + 1)

            household_id = input("Enter Household ID: ")

            consumption = float(
                input("Enter Water Consumption (KL): ")
            )

            if consumption < 0:
                print("Invalid consumption! Enter again.")
                return

            # Calculate charges
            slab_charge, penalty, total = calculate_bill(
                consumption
            )

            households.append({
                "id": household_id,
                "consumption": consumption,
                "slab_charge": slab_charge,
                "fixed_fee": FIXED_FEE,
                "penalty": penalty,
                "total": total
            })

        # Display individual bills
        print("\n========== WATER BILL DETAILS ==========")

        total_revenue = 0

        for h in households:

            print("\nHousehold ID :", h["id"])
            print("Consumption  :", h["consumption"], "KL")
            print("Slab Charges : Rs.", h["slab_charge"])
            print("Fixed Fee    : Rs.", h["fixed_fee"])
            print("Penalty      : Rs.", h["penalty"])
            print("Total Bill   : Rs.", h["total"])

            total_revenue += h["total"]

        # Consumption comparison
        print("\n========== CONSUMPTION ANALYSIS ==========")

        highest = max(
            households,
            key=lambda x: x["consumption"]
        )

        lowest = min(
            households,
            key=lambda x: x["consumption"]
        )

        average = sum(
            h["consumption"] for h in households
        ) / n

        print("Highest Consumption:")
        print(highest["id"], "-", highest["consumption"], "KL")

        print("\nLowest Consumption:")
        print(lowest["id"], "-", lowest["consumption"], "KL")

        print("\nAverage Consumption:", round(average, 2), "KL")

        # Identify excessive usage
        print("\nExcessive Water Usage Households:")

        found = False

        for h in households:
            if h["consumption"] > EXCESS_LIMIT:
                print(
                    h["id"],
                    "-",
                    h["consumption"],
                    "KL"
                )
                found = True

        if not found:
            print("No excessive water usage found.")

        # Final summary
        print("\n======================================")
        print("Total Water Bill Revenue: Rs.", total_revenue)
        print("Number of Households:", n)
        print("======================================")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")


# Execute program
water_tariff_analysis()
