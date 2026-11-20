# Input marks for five subjects
try:
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i} (0-100): "))
        if 0 <= mark <= 100:
            marks.append(mark)
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")
            exit()
    # Calculate total, average, and percentage
    total = sum(marks)
    average = total / len(marks)
    percentage = (total / 500) * 100
    # Assign grade based on average marks
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    # Display results
    print(f"Total Marks: {total}/500")
    print(f"Average Marks: {average}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
except ValueError:
    print("Invalid input. Please enter numeric values only.")