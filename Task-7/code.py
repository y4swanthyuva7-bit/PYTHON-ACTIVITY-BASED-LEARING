# Campus Resource Allocation Under Constraints

# Available campus resources
available = {
    "Projector": 5,
    "Laptop": 10,
    "Microphone": 6
}

activities = []

# Read number of activities
n = int(input("Enter number of activities: "))

# Read activity requirements
for i in range(n):

    print("\nActivity", i + 1)

    name = input("Enter activity name: ")
    priority = int(input("Enter priority (1 = Highest): "))

    print("Enter equipment requirements:")

    requirements = {}

    for equipment in available:
        quantity = int(input("Enter " + equipment + " required: "))
        requirements[equipment] = quantity

    activities.append({
        "name": name,
        "priority": priority,
        "requirements": requirements
    })


# Sort activities based on priority
activities.sort(key=lambda x: x["priority"])

# Store allocation details
allocation_report = []

# Allocate resources
for activity in activities:

    allocation = {}
    shortage = {}

    for equipment in available:

        required = activity["requirements"][equipment]

        allocated = min(required, available[equipment])

        shortage_quantity = required - allocated

        # Update available resources
        available[equipment] -= allocated

        allocation[equipment] = allocated
        shortage[equipment] = shortage_quantity

    allocation_report.append({
        "name": activity["name"],
        "priority": activity["priority"],
        "allocation": allocation,
        "shortage": shortage
    })


# Display allocation report
print("\n========== CAMPUS RESOURCE ALLOCATION REPORT ==========")

for report in allocation_report:

    print("\nActivity:", report["name"])
    print("Priority:", report["priority"])

    print("Allocated Resources:")

    for equipment, quantity in report["allocation"].items():
        print(equipment, ":", quantity)

    print("Shortage:")

    for equipment, quantity in report["shortage"].items():
        print(equipment, ":", quantity)


# Display remaining resources
print("\n========== REMAINING RESOURCES ==========")

for equipment, quantity in available.items():
    print(equipment, ":", quantity)

print("\n========== ALLOCATION COMPLETED ==========")
