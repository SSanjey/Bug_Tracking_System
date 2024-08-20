Bug Tracking System
Overview
The Bug Tracking System is a comprehensive application designed to manage and track bugs within a software development environment. It supports different roles including Admins, Managers, and Employees, each with specific functionalities to efficiently handle bug reporting, project management, and user accounts.

Features
Admin Module
Add Manager Account: Create new manager accounts.
View Manager Account: View details of existing manager accounts.
Delete Manager: Remove manager accounts from the system.
Update Manager Details: Modify details of existing manager accounts.
Add Employee Account: Create new employee accounts.
View Employee's Account: View details of existing employee accounts.
Delete Employee Account: Remove employee accounts from the system.
Update Employee Details: Modify details of existing employee accounts.
View All Projects: View a list of all projects in the system.
View Bug Reports: Access and review all bug reports.
Manager Panel
Update Profile: Update manager's profile information.
Manage Project: Oversee project-related activities.
Add Project: Create new projects.
View All Projects: View a list of all projects.
Delete Project: Remove projects from the system.
Update Project: Modify details of existing projects.
Bugs:
Add New Bug: Report a new bug.
View All Bugs: View all bug reports.
Update Bug: Modify details of existing bugs.
Delete Bug: Remove bug reports from the system.
Exit: Exit the manager panel.
Employee Panel
Update Profile: Update employee's profile information.
Add Bug Reports: Report new bugs (for testers only).
Update Bug Status: Modify the status of reported bugs.
View Bugs: View a list of bugs assigned to the employee.
Bug Details: View detailed information about specific bugs.
Exit: Exit the employee panel.
Database Schema
The Bug Tracking System uses a MySQL database named BDS (Bug Tracking System) with the following tables:

Table: Employee
empCode: int, Primary Key (used as username for login)
empName: varchar(30)
empEmail: varchar(40)
empPassword: varchar(20)
gender: varchar(10)
DOB: varchar(20)
mobileNo: bigint
Role: varchar(20) (e.g., manager, developer, tester, admin)
Table: AssignProject
projectID: int, Foreign Key
empCode: int, Foreign Key
Table: Project
projectID: int, Primary Key
projectName: varchar(30)
SDate: varchar(30)
EDate: varchar(30)
projectDesc: varchar(200)
Table: BugReport
bugNo: int, Primary Key
bugCode: int, Foreign Key
projectID: int, Foreign Key
TCode: int, Foreign Key
ECode: int, Foreign Key
status: varchar(20) (e.g., pending, resolved)
bugDesc: varchar(100)
Table: BugType
bugCode: int, Primary Key
bugCategory: varchar(30)
bugSeverity: varchar(20) (e.g., Critical, Major, Medium, Low)
Bug Codes and Their Descriptions
Functional Errors
Compilation Errors
Missing Commands
Runtime Errors
Communication Problems
Logical Errors
Inappropriate Error Handling
Calculation Issues
Files
setup_database.py: Initializes the database schema and sets up tables.
admin_module.py: Contains the Admin class for administrative functions.
admin_operations.py: Functions for handling administrative tasks.
manager_module.py: Contains the Manager class for manager functions.
manager_operations.py: Functions for managing bugs and projects.
employee_module.py: Contains the Employee class for employee functions.
employee_operations.py: Functions for managing bug reports and statuses.
main_application.py: Main entry point of the application, handling user interactions.
Setup Instructions
