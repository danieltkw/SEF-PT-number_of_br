# No additional libraries are required for this calculation

def calculate_linear_growth(x1, y1, x2, y2, x_target, residency_br_number):
    """
    Calculate the value at a target point and the adjusted total sum for a linear growth model.
    
    Parameters:
    - x1, y1: Coordinates of the initial point.
    - x2, y2: Coordinates of another point on the line.
    - x_target: The target point to calculate the value for.
    - residency_br_number: Additional constant to add to the final sum.
    
    Returns:
    - y_target: The value at the target point.
    - final_total: The adjusted total sum including the residency_br_number.
    """
    # Calculate the slope (m) and y-intercept (b) of the line
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m*x1

    # Calculate the target value for x_target
    y_target = m*x_target + b

    # Calculate the total sum of values from x = 1 to x_target
    n = x_target - 1  # Number of terms
    y_initial = m*1 + b  # Value at x = 1
    y_final = y_target  # Value at x_target
    total_sum = n/2 * (y_initial + y_final)  # Total sum of values

    # Adjust the total sum by adding the residency_br_number
    final_total = total_sum + residency_br_number

    return y_target, final_total

# Example usage
x1, y1 = 1, 5000
x2, y2 = 15, 23000
x_target = 20
residency_br_number = 400000
y_target, final_total = calculate_linear_growth(x1, y1, x2, y2, x_target, residency_br_number)

print(f"Value at point {x_target}: {y_target:.2f}k")
print(f"Adjusted total sum: {final_total:.2f}k")


# the sef have data from residency numbers = 400k+ 
# no data about illegals numbers, and no data about visa (!!!) numbers 
# poor data about last 50 years (+-medium age of pop in Portugal) of how much BR taken PT citizenship after some conditions (like living of family roots) 
# this is important because if you have any EU citizenship in PT (like Portuguese taken!), you disappear from the residency numbers! 
# probably there is ~1M BR living in PT (10% of total pop of PT) 
