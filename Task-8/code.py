# Campus Event Seating and Entry Validation

# Initialize seating capacity
rows = int(input("Enter number of rows: "))
seats_per_row = int(input("Enter seats per row: "))

# Create nested list for seating arrangement
seating = [[None for j in range(seats_per_row)]
           for i in range(rows)]

# Read registered participants
n = int(input("Enter number of registered participants: "))

registered_ids = []

for i in range(n):
    reg_id = input("Enter registration ID: ")
    registered_ids.append(reg_id)

# Track participant entries
entered_ids = []

valid_entries = []
invalid_entries = []
duplicate_entries = []

# Read number of ticket attempts
attempts = int(input("\nEnter number of ticket attempts: "))

for i in range(attempts):

    ticket_id = input("\nEnter ticket registration ID: ")

    # Validate registration ID
    if ticket_id not in registered_ids:
        print("Invalid ticket! Entry rejected.")
        invalid_entries.append(ticket_id)

    # Detect duplicate entries
    elif ticket_id in entered_ids:
        print("Duplicate entry detected!")
        duplicate_entries.append(ticket_id)

    else:
        # Find an available seat
        seat_assigned = False

        for r in range(rows):
            for s in range(seats_per_row):

                if seating[r][s] is None:

                    seating[r][s] = ticket_id
                    entered_ids.append(ticket_id)
                    valid_entries.append(ticket_id)

                    print("Entry successful!")
                    print("Assigned Seat: Row", r + 1,
                          "Seat", s + 1)

                    seat_assigned = True
                    break

            if seat_assigned:
                break

        if not seat_assigned:
            print("No seats available!")
            invalid_entries.append(ticket_id)


# Display seating arrangement
print("\n========== SEATING ARRANGEMENT ==========")

for r in range(rows):
    print("Row", r + 1, ":", seating[r])


# Calculate seating capacity
total_seats = rows * seats_per_row
occupied_seats = len(valid_entries)
available_seats = total_seats - occupied_seats

# Display entry report
print("\n========== EVENT ENTRY REPORT ==========")

print("Total Seating Capacity:", total_seats)
print("Occupied Seats:", occupied_seats)
print("Available Seats:", available_seats)

print("\nValid Entries:", valid_entries)
print("Invalid Entries:", invalid_entries)
print("Duplicate Entries:", duplicate_entries)

print("\n========== EVENT AUDIT COMPLETED ==========")
