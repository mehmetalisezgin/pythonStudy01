a = 20
b = 30
c = 45
salary = a * b* c
print('The Given Salary is ', salary)
print('Mehmet Ali')

list=[1,"mehmet","erva","asli",5,4,8,5,100.125]
print(list[0])
#[star : end ] start is inclusive but end is exclusive
print(list[0:2])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[7]
# Print the variable eat_sleep_area
print(eat_sleep_area)

# Use slicing to create downstairs
downstairs=areas[0:6]

# Use slicing to create upstairs
upstairs=areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
print(x[2][0])
print(x[2][:2])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[9] = 10.50
print(areas)

# Change "living room" to "chill zone"
areas[4] = "chill zone"
print(areas)

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas_copy)
print(areas)
print(max(areas))

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
print(out2)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first+second

# Sort full in descending order: full_sorted
#when you set the reverse parameter to True, it sorts the list in the opposite direction, i.e.,
# descending order (largest to smallest).
full_sorted = sorted(full , reverse = True)

# Print out full_sorted
print(full_sorted)

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0

print(areas.index(20.0))
# Print out how often 9.50 appears in areas
print(areas.count(9.50))
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size

areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)


