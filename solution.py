print("Courier Booking")

cities = ["Delhi", "Mumbai", "Pune"]
charges = [100, 150, 120]

from_city = input("From city: ")
to_city = input("To city: ")

if from_city in cities and to_city in cities:
    weight = int(input("Enter weight: "))
    amount = weight * 50
else:
    print("City not available")
    amount = 0

print("From:", from_city)
print("To:", to_city)
print("Amount:", amount)

for i in range(3):
    print("Booked")

print("End")

Output:
Courier Booking
From city: Delhi
To city: Mumbai
Enter weight: 2
From: Delhi
To: Mumbai
Amount: 100
Booked
Booked
Booked
End
