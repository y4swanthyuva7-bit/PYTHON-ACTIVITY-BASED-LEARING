# Progressive Electricity Billing System

def calculate_energy_charge(units):
    charge = 0

    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    return charge


def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)

    fixed_charge = 50
    surcharge = energy_charge * 0.05

    if units < 100:
        rebate = energy_charge * 0.02
    else:
        rebate = 0

    total_bill = (
        energy_charge
        + fixed_charge
        + surcharge
        - rebate
    )

    return energy_charge, fixed_charge, surcharge, rebate, total_bill


# Main program

monthly_data = []

months = int(input("Enter number of months: "))

for i in range(months):

    print("\nMonth", i + 1)

    units = int(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units! Enter a non-negative value.")
        break

    energy, fixed, surcharge, rebate, total = calculate_bill(units)

    monthly_data.append({
        "month": i + 1,
        "units": units,
        "energy": energy,
        "fixed": fixed,
        "surcharge": surcharge,
        "rebate": rebate,
        "total": total
    })

    print("Energy Charge: Rs.", round(energy, 2))
    print("Fixed Charge: Rs.", round(fixed, 2))
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total, 2))


# Compare monthly bills

print("\n========== MONTHLY BILL COMPARISON ==========")

for i in range(len(monthly_data)):

    current = monthly_data[i]

    print("\nMonth", current["month"],
          "- Bill: Rs.", round(current["total"], 2))

    if i > 0:

        previous = monthly_data[i - 1]

        increase = current["total"] - previous["total"]

        if previous["total"] > 0:
            percentage = (increase / previous["total"]) * 100
        else:
            percentage = 0

        print("Bill Change: Rs.", round(increase, 2))
        print("Percentage Change:", round(percentage, 2), "%")

        if percentage > 30:
            print("WARNING: Unusual increase in electricity bill!")
        else:
            print("Bill Status: Normal")

print("\n========== PROGRAM COMPLETED ==========")
