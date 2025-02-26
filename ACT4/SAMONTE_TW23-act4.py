records = []
filename = None

while True:
    print("\nMenu:")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Order by Last Name")
    print("6. Order by Grade")
    print("7. Show Student Record")
    print("8. Add Record")
    print("9. Edit Record")
    print("10. Delete Record")
    print("11. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        filename = input("Enter filename to open: ")
        try:
            with open(filename, 'r') as file:
                records = []
                for line in file:
                    parts = line.strip().split(',')
                    student_id = parts[0]
                    full_name = (parts[1], parts[2])
                    class_standing = float(parts[3])
                    major_exam_grade = float(parts[4])
                    records.append((student_id, full_name, class_standing, major_exam_grade))
            print(f"File '{filename}' opened successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' does not exist.")

    elif choice == '2':
        if filename:
            with open(filename, 'w') as file:
                for record in records:
                    line = f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n"
                    file.write(line)
            print(f"Records saved to '{filename}'.")
        else:
            print("No file is currently open. Use 'Save As' to save the records.")

    elif choice == '3':
        filename = input("Enter filename to save as: ")
        with open(filename, 'w') as file:
            for record in records:
                line = f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n"
                file.write(line)
        print(f"Records saved to '{filename}'.")

    elif choice == '4':
        if not records:
            print("No records to display.")
        else:
            for record in records:
                print(record)

    elif choice == '5':
        sorted_records = sorted(records, key=lambda x: x[1][1])  # Sort by last name
        for record in sorted_records:
            print(record)

    elif choice == '6':
        def calculate_grade(record):
            class_standing = record[2]
            major_exam_grade = record[3]
            return (0.6 * class_standing) + (0.4 * major_exam_grade)

        sorted_records = sorted(records, key=calculate_grade)
        for record in sorted_records:
            print(record)

    elif choice == '7':
        student_id = input("Enter Student ID: ")
        found = False
        for record in records:
            if record[0] == student_id:
                print(record)
                found = True
                break
        if not found:
            print("Student record not found.")

    elif choice == '8':
        student_id = input("Enter Student ID (6 digits): ")
        full_name = (input("Enter First Name: "), input("Enter Last Name: "))
        class_standing = float(input("Enter Class Standing: "))
        major_exam_grade = float(input("Enter Major Exam Grade: "))
        
        if any(record[0] == student_id for record in records):
            print("Record with this Student ID already exists.")
        else:
            records.append((student_id, full_name, class_standing, major_exam_grade))
            print("Record added successfully.")

    elif choice == '9':
        student_id = input("Enter Student ID to edit: ")
        found = False
        for i, record in enumerate(records):
            if record[0] == student_id:
                new_full_name = (input("Enter new First Name: "), input("Enter new Last Name: "))
                new_class_standing = float(input("Enter new Class Standing: "))
                new_major_exam_grade = float(input("Enter new Major Exam Grade: "))
                records[i] = (student_id, new_full_name, new_class_standing, new_major_exam_grade)
                print("Record updated successfully.")
                found = True
                break
        if not found:
            print("Student record not found.")

    elif choice == '10':
        student_id = input("Enter Student ID to delete: ")
        found = False
        for i, record in enumerate(records):
            if record[0] == student_id:
                del records[i]
                print("Record deleted successfully.")
                found = True
                break
        if not found:
            print("Student record not found.")

    elif choice == '11':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")