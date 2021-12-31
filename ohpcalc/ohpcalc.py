# Change Order Request Calculator
# 1. Request Subtotal Value of the Change Order Request
# 2. Request OHP Percentage Value
# 3. Request Tax Status of Project
# 4. If job is taxable, request material value to calculate sales tax
# 4a. If Taxable, calculate sales tax value
# 4b. If Tax Exempt, sales tax value to be 0.00
# 5. Compute OHP & Tax Values (based on status)
# 6. Adjust OHP Value so that Total of Change Order Request is Rounded to Nearest $1.00
# 7. Print Values of Subtotal, Material Value, Tax Value, Original OHP, Revised OHP, Total of COR

import math, os

# Rounding Tool to Round Up if Greater Than .5 or Down if Less Than .5
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier

def main():
    # Request Subtotal Value of COR
    while True:
        try:
            subtotal = float(input("What is the subtotal value of materials and labor of COR? ($0.00) $"))
            break
        except ValueError:
            print("Please input decimal number only in this format XXXX.XX")
            continue

    # Request the Overhead & Profit Rate to be used
    while True:
        try:
           ohp_percentage = float(input("What is the Overhead & Profit rate? (0%) "))
           break
        except ValueError:
            print("Please input whole number only without % or decimal points")
            continue

    # Check the project's tax status
    tax_status = input("Is this job tax-exempt? (Y/N) ")

    # JOB IS TAXABLE
    if tax_status == 'N':
        material_value = float(input("What is the material value of COR? ($0.00) $"))
        tax_value = round((material_value * 0.08375),2)

    # JOB IS TAX EXEMPT
    else:
        tax_value = round(0.00,2)

    ohp_value = round((subtotal * (ohp_percentage/100)),2)

    total_value = ohp_value + subtotal + tax_value

    rounded_total = float("{:.2f}".format(round_half_up(total_value)))
    rounded_ohp = float("{:.2f}".format(rounded_total - total_value + ohp_value))

    # Clear the Input Screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print Calculations
    print("Change Order Calculations")
    print("Subtotal: ", "{:.2f}".format(subtotal))
    if tax_status == 'N':
        print("Material Value: ", "{:.2f}".format(material_value))
        print("Sales Tax: ", "{:.2f}".format(tax_value))
    print("Overhead & Profit: ", "{:.2f}".format(ohp_value))
    print("Total: ", "{:.2f}".format(total_value))
    print("\nRounded Total: ", "{:.2f}".format(rounded_total))
    print("Rounded Overhead & Profit: ", "{:.2f}".format(rounded_ohp))

    # Keep Screen Open to read Values
    print("\nThanks for Using the OHP Calculator!")
    input('Press Enter to Exit...')
