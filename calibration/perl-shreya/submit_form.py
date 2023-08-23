#!/usr/bin/env python3

import cgi

def get_remaining_days(calibration_days):
    try:
        # Try to convert calibration_days to an integer
        calibration_days = int(calibration_days)
    except (ValueError, TypeError):
        # Handle the situation where calibration_days is not a valid integer
        calibration_days = 0

    # Here you can implement the logic to calculate the remaining days
    # For example, you can use the current date and calculate the difference
    # between the calibration date and the current date.
    remaining_days = 0  # Replace this with the actual remaining days
    return remaining_days

print("Content-type: text/html\n")

form = cgi.FieldStorage()

plant = form.getvalue('plant')
area = form.getvalue('area')
part_type = form.getvalue('partType')
part_unique_no = form.getvalue('partUniqueNo')
calibration_days = form.getvalue('calibrationDays')
remarks = form.getvalue('remarks')

# Validate and process the form data (you can add more validation as needed)
if plant and area and part_type and part_unique_no and calibration_days and remarks:
    # Write the data to a file (replace "data.txt" with the desired filename)
    with open('data.txt', 'a') as f:
        f.write(f"{plant}, {area}, {part_type}, {part_unique_no}, {calibration_days}, {remarks}\n")

# Calculate the remaining days
remaining_days = get_remaining_days(calibration_days)

# Redirect to the confirmation page
print(f"Location: confirmation.html?plant={plant}&area={area}&partType={part_type}&partUniqueNo={part_unique_no}&calibrationDays={calibration_days}&remarks={remarks}&remainingDays={remaining_days}\n\n")