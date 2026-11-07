print("Type your numbers separated by a space (e.g., 5 10 15 20)")
print("Type 'exit' to quit.")

while True:
    user_input = input("\nEnter numbers: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        
        numbers = [float(x) for x in user_input.split()]
        
        if not numbers:
            print("Please enter at least one number.")
            continue

        
        total = sum(numbers)
        count = len(numbers)
        average = total / count

        
        print(f"Total Sum: {total}")
        print(f"Average:   {average}")
        
    except ValueError:
        print("Invalid input. Please use numbers and spaces only.")
