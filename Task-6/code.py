
import math

# Function to calculate distance using Haversine formula
def calculate_distance(point1, point2):

    lat1, lon1 = point1
    lat2, lon2 = point2

    # Convert degrees into radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (math.sin(dlat / 2) ** 2 +
         math.cos(lat1) * math.cos(lat2) *
         math.sin(dlon / 2) ** 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Earth's radius in kilometers
    R = 6371

    distance = R * c

    return distance


# Main program
n = int(input("Enter number of locations: "))

locations = []

# Read geographical coordinates
for i in range(n):
    print("\nLocation", i + 1)

    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    # Store coordinates as tuple
    locations.append((latitude, longitude))


# Calculate distances between successive points
distances = []

for i in range(n - 1):

    distance = calculate_distance(
        locations[i],
        locations[i + 1]
    )

    distances.append(distance)


# Display route distances
print("\n========== ROUTE DISTANCE ANALYSIS ==========")

for i in range(len(distances)):
    print("Segment", i + 1,
          ":", round(distances[i], 2), "km")


# Identify longest route segment
if distances:

    max_distance = max(distances)
    max_index = distances.index(max_distance)

    print("\nLongest Route Segment:")
    print("From Location", max_index + 1,
          "to Location", max_index + 2)

    print("Distance:", round(max_distance, 2), "km")

else:
    print("\nNot enough locations to calculate distance.")

print("\n========== ANALYSIS COMPLETED ==========")
