# University Hostel Room Allocation System

# Step 1: Initialize hostel rooms
rooms = [
    {"room": "R101", "capacity": 2,
     "gender": "Boys", "students": []},

    {"room": "R102", "capacity": 3,
     "gender": "Girls", "students": []},

    {"room": "R103", "capacity": 2,
     "gender": "Boys", "students": []},

    {"room": "R104", "capacity": 3,
     "gender": "Girls", "students": []}
]

# Step 2: Initialize student details
students = [
    ("S101", "Boys", "GroupA"),
    ("S102", "Boys", "GroupA"),
    ("S103", "Girls", "GroupB"),
    ("S104", "Girls", "GroupB"),
    ("S105", "Boys", "GroupC"),
    ("S106", "Girls", "GroupD"),
    ("S107", "Boys", "GroupC"),
    ("S108", "Girls", "GroupD"),
    ("S109", "Boys", "GroupE"),
    ("S110", "Girls", "GroupF")
]

# Step 3: Initialize tracking lists
assigned_students = []
unallocated_students = []
duplicate_assignments = []

# Step 4: Allocate students
for student in students:

    student_id, gender, group = student

    # Check duplicate student assignment
    if student_id in assigned_students:
        duplicate_assignments.append(student_id)
        continue

    allocated = False

    # Search for a suitable room
    for room in rooms:

        # Check eligibility
        if room["gender"] != gender:
            continue

        # Check room capacity
        if len(room["students"]) >= room["capacity"]:
            continue

        # Check grouping constraint
        if room["students"]:
            existing_group = room["students"][0][1]

            if existing_group != group:
                continue

        # Allocate student
        room["students"].append((student_id, group))
        assigned_students.append(student_id)

        print(student_id, "allocated to", room["room"])

        allocated = True
        break

    # Record unallocated student
    if not allocated:
        unallocated_students.append(student_id)


# Step 5: Display allocation report
print("\n========== HOSTEL ALLOCATION REPORT ==========")

for room in rooms:

    print("\nRoom Number:", room["room"])
    print("Eligibility:", room["gender"])
    print("Capacity:", room["capacity"])

    print("Allocated Students:")

    if room["students"]:
        for student in room["students"]:
            print(student[0], "-", student[1])
    else:
        print("No students allocated")

    occupied = len(room["students"])
    available = room["capacity"] - occupied

    print("Occupied Seats:", occupied)
    print("Available Seats:", available)


# Step 6: Calculate total capacity
total_capacity = sum(room["capacity"] for room in rooms)

total_students = len(students)
total_allocated = len(assigned_students)
unallocated_demand = len(unallocated_students)

# Step 7: Display final summary
print("\n========== FINAL ALLOCATION SUMMARY ==========")

print("Total Hostel Capacity:", total_capacity)
print("Total Students:", total_students)
print("Total Allocated:", total_allocated)
print("Unallocated Demand:", unallocated_demand)

print("Unallocated Students:", unallocated_students)

print("Duplicate Assignments:", duplicate_assignments)

print("\n========== ALLOCATION COMPLETED ==========")
