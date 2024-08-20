from manager_module import Manager

def display_menu():
    print("\nManager Panel")
    print("1. Update Profile")
    print("2. Manage Project")
    print("   1. Add Project")
    print("   2. View All Projects")
    print("   3. Delete Project")
    print("   4. Update Project")
    print("3. Bug's")
    print("   1. Add New Bug")
    print("   2. View All Bug’s")
    print("   3. Update Bug")
    print("   4. Delete Bug")
    print("4. Exit")

def handle_profile_operations(manager):
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
            manager.update_profile(empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
        
        elif choice == '2':
            break

def handle_project_operations(manager):
    while True:
        print("\nProject Management")
        print("1. Add Project")
        print("2. View All Projects")
        print("3. Delete Project")
        print("4. Update Project")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            projectID = input("Enter Project ID: ")
            projectName = input("Enter Project Name: ")
            SDate = input("Enter Start Date (YYYY-MM-DD): ")
            EDate = input("Enter End Date (YYYY-MM-DD): ")
            projectDec = input("Enter Project Description: ")
            manager.add_project(projectID, projectName, SDate, EDate, projectDec)
        
        elif choice == '2':
            projects = manager.view_all_projects()
            print("Projects:")
            for project in projects:
                print(project)
        
        elif choice == '3':
            projectID = input("Enter Project ID to delete: ")
            manager.delete_project(projectID)
        
        elif choice == '4':
            projectID = input("Enter Project ID to update: ")
            projectName = input("Enter new Project Name: ")
            SDate = input("Enter new Start Date (YYYY-MM-DD): ")
            EDate = input("Enter new End Date (YYYY-MM-DD): ")
            projectDec = input("Enter new Project Description: ")
            manager.update_project(projectID, projectName, SDate, EDate, projectDec)
        
        elif choice == '5':
            break

def handle_bug_operations(manager):
    while True:
        print("\nBug Management")
        print("1. Add New Bug")
        print("2. View All Bugs")
        print("3. Update Bug")
        print("4. Delete Bug")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            bugNo = input("Enter Bug Number: ")
            bugCode = input("Enter Bug Code: ")
            projectID = input("Enter Project ID: ")
            TCode = input("Enter Tester Code: ")
            ECode = input("Enter Engineer Code: ")
            status = input("Enter Status: ")
            bugDes = input("Enter Bug Description: ")
            manager.add_bug(bugNo, bugCode, projectID, TCode, ECode, status, bugDes)
        
        elif choice == '2':
            bugs = manager.view_all_bugs()
            print("Bugs:")
            for bug in bugs:
                print(bug)
        
        elif choice == '3':
            bugNo = input("Enter Bug Number to update: ")
            status = input("Enter new Status: ")
            bugDes = input("Enter new Bug Description: ")
            manager.update_bug(bugNo, status, bugDes)
        
        elif choice == '4':
            bugNo = input("Enter Bug Number to delete: ")
            manager.delete_bug(bugNo)
        
        elif choice == '5':
            break

def main():
    manager = Manager()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            handle_profile_operations(manager)
        
        elif choice == '2':
            handle_project_operations(manager)
        
        elif choice == '3':
            handle_bug_operations(manager)
        
        elif choice == '4':
            print("Exiting...")
            manager.close_connection()
            break

if __name__ == "__main__":
    main()
