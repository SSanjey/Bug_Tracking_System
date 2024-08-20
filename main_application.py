# Import statements should be at the top of the file
from admin_module import Admin
from manager_module import Manager
from employee_module import Employee
from setup_database import setup_database
from admin_operations import handle_employee_operations
from manager_operations import handle_bug_operations as manager_bug_ops
from employee_operations import handle_bug_operations as employee_bug_ops

def main():
    setup_database()
    
    # Initialize connections
    admin = Admin()
    manager = Manager()
    employee = Employee()
    
    while True:
        print("\nMain Menu")
        print("1. Admin Panel")
        print("2. Manager Panel")
        print("3. Employee Panel")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            # Handle admin operations
            handle_employee_operations(admin)
        
        elif choice == '2':
            # Handle manager operations
            manager_bug_ops(manager)  # Use the alias if necessary
        
        elif choice == '3':
            # Handle employee operations
            employee_bug_ops(employee)  # Use the alias if necessary
        
        elif choice == '4':
            # Close connections before exiting
            admin.close_connection()
            manager.close_connection()
            employee.close_connection()
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
