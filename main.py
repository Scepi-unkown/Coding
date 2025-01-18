def calculate_bill(units):
    if units <= 100:
        rate = 1.5
    elif units <= 200:
        rate = 2.5
    elif units <= 500:
        rate = 4.0
    else:
        rate = 6.0

    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    elif units <= 500:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4.0)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (300 * 4.0) + ((units - 500) * 6.0)

    return bill

try:
    units_consumed = float(input("Enter the number of units consumed: "))
    if units_consumed < 0:
        print("Units consumed cannot be negative.")
    else:
        total_bill = calculate_bill(units_consumed)
        print(f"Your electricity bill for {units_consumed} units is: ₹{total_bill:.2f}")
except ValueError:
    print("Invalid input! Please enter a numeric value for units.")