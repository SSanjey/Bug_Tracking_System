from employee_module import Employee

def display_menu():
    print("\nEmployee Panel")
    print("1. Update Profile")
    print("2. Add Bug's Report")  # Hint: Only for testers
    print("3. Update Bug Status")
    print("4. View Bugs")
    print("5. Bug Details")
    print("6. Exit")

def handle_profile_operations(employee):
    while True:
        print("\nProfile Operations")
        print("1. Update Profile")
        print("2. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            empCode = input("Enter Employee Code: ")
            empName = input("Enter new Employee Name: ")
            empEmail = input("Enter new Employee Email: ")
            empPassword = input("Enter new Employee Password: ")
            gender = input("Enter new Gender: ")
            DOB = input("Enter new Date of Birth (YYYY-MM-DD): ")
            mobileNo = input("Enter new Mobile Number: ")
            Role = input("Enter new Role: ")
            employee.update_profile(empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
            print("Profile updated successfully.")
        
        elif choice == '2':
            break

def handle_bug_operations(employee):
    while True:
        print("\nBug Management")
        print("1. Add Bug's Report")  # Hint: Only for testers
        print("2. Update Bug Status")
        print("3. View Bugs")
        print("4. Bug Details")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            # Assuming only testers can add bugs
            role = input("Enter your role (tester/engineer): ").lower()
            if role == 'tester':
                bugNo = input("Enter Bug Number: ")
                bugCode = input("Enter Bug Code: ")
                projectID = input("Enter Project ID: ")
                TCode = input("Enter Tester Code: ")
                ECode = input("Enter Engineer Code: ")
                status = input("Enter Status: ")
                bugDes = input("Enter Bug Description: ")
                employee.add_bug(bugNo, bugCode, projectID, TCode, ECode, status, bugDes)
                print("Bug added successfully.")
            else:
                print("Only testers can add bugs.")
        
        elif choice == '2':
            bugNo = input("Enter Bug Number to update status: ")
            status = input("Enter new Status: ")
            bugDes = input("Enter new Bug Description: ")
            employee.update_bug(bugNo, status, bugDes)
            print("Bug updated successfully.")
        
        elif choice == '3':
            bugs = employee.view_all_bugs()
            print("Bugs:")
            for bug in bugs:
                print(bug)
        
        elif choice == '4':
            bugNo = input("Enter Bug Number to view details: ")
            bug_details = employee.view_bug_details(bugNo)
            print("Bug Details:")
            print(bug_details)
        
        elif choice == '5':
            break

def main():
    employee = Employee()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            handle_profile_operations(employee)
        
        elif choice == '2' or choice == '3' or choice == '4' or choice == '5':
            handle_bug_operations(employee)
        
        elif choice == '6':
            print("Exiting...")
            employee.close_connection()
            break

if __name__ == "__main__":
    main()
