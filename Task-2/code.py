# Smart Campus Incident and Maintenance Prioritization

# Step 1: Define severity points
severity_points = {
    "High": 5,
    "Medium": 3,
    "Low": 1
}

# Step 2: Define location points
location_points = {
    "Laboratory": 5,
    "Classroom": 4,
    "Library": 3,
    "Corridor": 2,
    "Other": 1
}

incidents = []

# Step 3: Read number of incidents
n = int(input("Enter number of maintenance reports: "))

# Step 4: Collect incident details
for i in range(n):

    print("\nIncident", i + 1)

    incident_id = input("Enter incident ID: ")
    description = input("Enter incident description: ")

    severity = input(
        "Enter severity (High/Medium/Low): "
    ).title()

    location = input(
        "Enter location (Laboratory/Classroom/Library/Corridor/Other): "
    ).title()

    frequency = int(
        input("Enter reported frequency: ")
    )

    # Validate input
    if severity not in severity_points:
        print("Invalid severity! Report ignored.")
        continue

    if location not in location_points:
        print("Invalid location! Report ignored.")
        continue

    if frequency <= 0:
        print("Invalid frequency! Report ignored.")
        continue

    # Step 5: Calculate priority score
    score = (
        severity_points[severity] * 5
        + location_points[location] * 3
        + frequency * 2
    )

    # Step 6: Classify priority
    if score >= 40:
        priority = "Critical"
    elif score >= 25:
        priority = "Medium"
    else:
        priority = "Low"

    # Store incident details
    incidents.append({
        "id": incident_id,
        "description": description,
        "severity": severity,
        "location": location,
        "frequency": frequency,
        "score": score,
        "priority": priority
    })


# Step 7: Sort incidents by priority score
incidents.sort(
    key=lambda x: x["score"],
    reverse=True
)


# Step 8: Display ranked incident report
print("\n========== CAMPUS MAINTENANCE REPORT ==========")

for i, incident in enumerate(incidents, start=1):

    print("\nRank:", i)
    print("Incident ID:", incident["id"])
    print("Description:", incident["description"])
    print("Severity:", incident["severity"])
    print("Location:", incident["location"])
    print("Reported Frequency:", incident["frequency"])
    print("Priority Score:", incident["score"])
    print("Priority Level:", incident["priority"])


# Step 9: Calculate priority summary
critical_count = 0
medium_count = 0
low_count = 0

for incident in incidents:

    if incident["priority"] == "Critical":
        critical_count += 1

    elif incident["priority"] == "Medium":
        medium_count += 1

    else:
        low_count += 1


# Step 10: Display final summary
print("\n========== PRIORITY SUMMARY ==========")

print("Total Valid Incidents:", len(incidents))
print("Critical Priority Cases:", critical_count)
print("Medium Priority Cases:", medium_count)
print("Low Priority Cases:", low_count)

if incidents:
    print("\nHighest Priority Incident:",
          incidents[0]["id"])

print("\n========== ANALYSIS COMPLETED ==========")
