number_of_commands = int(input())

parking = {}

for _ in range(number_of_commands):
    data = input()
    split_data = data.split()
    command = split_data[0]

    if command == "register":
        username = split_data[1]
        license_plate_number = split_data[2]

        if username in parking:  # if a user tries to register another license plate using the same username
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")


    elif command == "unregister":
        username = split_data[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]  # parking.pop(username)
            print(f"{username} unregistered successfully")

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")
