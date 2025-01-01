def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:
        return 0  # Handle ZeroDivisionError
    except TypeError:
        return "Error: Non-numeric data found"

# Example usage
data = [1, 2, 3, 4, 0]
average = calculate_average(data)
print(f"Average: {average}")

data = []
average = calculate_average(data)
print(f"Average: {average}")

data = [1,2,'a']
average = calculate_average(data)
print(f"Average: {average}")