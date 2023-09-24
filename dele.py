import datetime
import math
from tkinter import messagebox

def calculate_charge(vehicle_type, checkin_time, checkout_time):
    duration = checkout_time - checkin_time
    hours = duration.total_seconds() / 3600  # Convert duration to hours

    if vehicle_type == "TwoWheeler":
        charge = hours * 20
    elif vehicle_type == "ThreeWheeler":
        charge = hours * 30
    elif vehicle_type == "FourWheeler":
        charge = hours * 50
    else:
        charge = hours * 60

    rounded_charge = math.ceil(charge)

    return rounded_charge

def delete_record(token, vehicle_number, vehicle_type):
    with open('vehicle_records.txt', 'r') as file:
        records = file.readlines()

    new_records = []
    deleted = False
    checkout_time = datetime.datetime.now()

    for record in records:
        tokens = record.split('|')
        if tokens[3] == token and tokens[1] == vehicle_number and tokens[4].strip() == vehicle_type:
            checkin_time = datetime.datetime.strptime(tokens[2], "%Y:%m:%d %H:%M:%S")
            charge = calculate_charge(vehicle_type, checkin_time, checkout_time)
            messagebox.showinfo("Charge", f"Charge: {charge}")
            deleted = True
        else:
            new_records.append(record)

    if deleted:
        with open('vehicle_records.txt', 'w') as file:
            file.writelines(new_records)
    else:
        messagebox.showwarning("Error", "Vehicle record not found.")

# Test the delete_record function
if __name__ == "__main__":
    # Example usage
    token = input("Enter token number: ")
    vehicle_number = input("Enter vehicle number: ")
    vehicle_type = input("Enter vehicle type: ")

    delete_record(token, vehicle_number, vehicle_type)
