from admin_module import Admin

def display_menu():
    print("\nAdmin Module")
    print("1. Manager")
    print("   1. Add Manager Account")
    print("   2. View Manager Account")
    print("   3. Delete Manager")
    print("   4. Update Manager Details")
    print("2. Employee")
    print("   1. Add Employee Account")
    print("   2. View Employee's Account")
    print("   3. Delete Employee Account")
    print("   4. Update Employee Details")
    print("3. View All Projects")
    print("4. View Bug Reports")
    print("5. Exit")

def handle_manager_operations(admin):
    while True:
        print("\nManager Operations")
        print("1. Add Manager Account")
        print("2. View Manager Account")
        print("3. Delete Manager")
        print("4. Update Manager Details")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            empCode = int(input("Enter Employee Code: "))
            empName = input("Enter Employee Name: ")
            empEmail = input("Enter Employee Email: ")
            empPassword = input("Enter Employee Password: ")
            gender = input("Enter Gender: ")
            DOB = input("Enter Date of Birth (YYYY-MM-DD): ")
            mobileNo = int(input("Enter Mobile Number: "))
            Role = 'manager'
            admin.add_manager(empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
            print("Manager added successfully.")
        
        elif choice == '2':
            managers = admin.view_manager()
            print("Managers:")
            for manager in managers:
                print(manager)
        
        elif choice == '3':
            empCode = int(input("Enter Employee Code to delete: "))
            admin.delete_manager(empCode)
            print("Manager deleted successfully.")
        
        elif choice == '4':
            empCode = int(input("Enter Employee Code to update: "))
            empName = input("Enter new Employee Name: ")
            empEmail = input("Enter new Employee Email: ")
            empPassword = input("Enter new Employee Password: ")
            gender = input("Enter new Gender: ")
            DOB = input("Enter new Date of Birth (YYYY-MM-DD): ")
            mobileNo = int(input("Enter new Mobile Number: "))
            Role = 'manager'
            admin.update_manager(empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
            print("Manager updated successfully.")
        
        elif choice == '5':
            break

def handle_employee_operations(admin):
    while True:
        print("\nEmployee Operations")
        print("1. Add Employee Account")
        print("2. View Employee's Account")
        print("3. Delete Employee Account")
        print("4. Update Employee Details")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            empCode = int(input("Enter Employee Code: "))
            empName = input("Enter Employee Name: ")
            empEmail = input("Enter Employee Email: ")
            empPassword = input("Enter Employee Password: ")
            gender = input("Enter Gender: ")
            DOB = input("Enter Date of Birth (YYYY-MM-DD): ")
            mobileNo = int(input("Enter Mobile Number: "))
            Role = input("Enter Role: ")
            admin.add_employee(empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
            print("Employee added successfully.")
        
        elif choice == '2':
            employees = admin.view_employee()
            print("Employees:")
            for employee in employees:
                print(employee)
        
        elif choice == '3':
            empCode = int(input("Enter Employee Code to delete: "))
            admin.delete_employee(empCode)
            print("Employee deleted successfully.")
        
        elif choice == '4':
            empCode = int(input("Enter Employee Code to update: "))
            empName = input("Enter new Employee Name: ")
            empEmail = input("Enter new Employee Email: ")
            empPassword = input("Enter new Employee Password: ")
            gender = input("Enter new Gender: ")
            DOB = input("Enter new Date of Birth (YYYY-MM-DD): ")
            mobileNo = int(input("Enter new Mobile Number: "))
            Role = input("Enter new Role: ")
            admin.update_employee(empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
            print("Employee updated successfully.")
        
        elif choice == '5':
            break

def main():
    admin = Admin()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            handle_manager_operations(admin)
        
        elif choice == '2':
            handle_employee_operations(admin)
        
        elif choice == '3':
            projects = admin.view_all_projects()
            print("Projects:")
            for project in projects:
                print(project)
        
        elif choice == '4':
            bug_reports = admin.view_bug_reports()
            print("Bug Reports:")
            for report in bug_reports:
                print(report)
        
        elif choice == '5':
            admin.close_connection()
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
