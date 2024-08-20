import mysql.connector

def setup_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sanjey123@",
        database="BDS",
        port=3306
    )
    cursor = conn.cursor()

    # Drop existing tables
    cursor.execute('''DROP TABLE IF EXISTS AssignProject''')
    cursor.execute('''DROP TABLE IF EXISTS BugReport''')
    cursor.execute('''DROP TABLE IF EXISTS BugType''')
    cursor.execute('''DROP TABLE IF EXISTS Employee''')
    cursor.execute('''DROP TABLE IF EXISTS Project''')

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS Project (
        projectID INT PRIMARY KEY,
        projectName VARCHAR(30),
        SDate VARCHAR(30),
        EDate VARCHAR(30),
        projectDec VARCHAR(200)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
        empCode INT PRIMARY KEY,
        empName VARCHAR(30),
        empEmail VARCHAR(40),
        empPassword VARCHAR(20),
        gender VARCHAR(10),
        DOB VARCHAR(20),
        mobileNo BIGINT,
        Role VARCHAR(20)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS AssignProject (
        projectID INT,
        empCode INT,
        FOREIGN KEY (projectID) REFERENCES Project(projectID),
        FOREIGN KEY (empCode) REFERENCES Employee(empCode)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS BugType (
        bugCode INT PRIMARY KEY,
        bugCategory VARCHAR(30),
        bugSeverity VARCHAR(20)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS BugReport (
        bugNo INT PRIMARY KEY,
        bugCode INT,
        projectID INT,
        TCode INT,
        ECode INT,
        status VARCHAR(20),
        bugDes VARCHAR(100),
        FOREIGN KEY (bugCode) REFERENCES BugType(bugCode),
        FOREIGN KEY (projectID) REFERENCES Project(projectID),
        FOREIGN KEY (TCode) REFERENCES Employee(empCode),
        FOREIGN KEY (ECode) REFERENCES Employee(empCode)
    )''')

    # Commit schema changes
    conn.commit()

    # Sample data to be inserted
    employee_data = [
        (1, 'Alice Johnson', 'alice.johnson@example.com', 'password123', 'Female', '1985-03-15', 9876543210, 'manager'),
        (2, 'Bob Smith', 'bob.smith@example.com', 'password123', 'Male', '1990-06-25', 9123456789, 'developer'),
        (3, 'Carol White', 'carol.white@example.com', 'password123', 'Female', '1992-08-10', 9234567890, 'tester'),
        (4, 'David Brown', 'david.brown@example.com', 'password123', 'Male', '1988-11-05', 9345678901, 'tester'),
        (5, 'Emma Wilson', 'emma.wilson@example.com', 'password123', 'Female', '1995-01-20', 9456789012, 'developer')
    ]

    project_data = [
        (1, 'Project Alpha', '2024-01-01', '2024-12-31', 'A project to develop a new AI-based application.'),
        (2, 'Project Beta', '2024-02-01', '2024-11-30', 'A project focused on enhancing existing web services.'),
        (3, 'Project Gamma', '2024-03-01', '2024-10-15', 'A project to create a new e-commerce platform.')
    ]

    bugtype_data = [
        (1, 'Functional Errors', 'Critical'),
        (2, 'Compilation Errors', 'Major'),
        (3, 'Missing commands', 'Medium'),
        (4, 'Run time Errors', 'Critical'),
        (5, 'Communication problems', 'Low'),
        (6, 'Logical errors', 'Major'),
        (7, 'Inappropriate error handling', 'Medium'),
        (8, 'Calculation issues', 'Critical')
    ]

    bugreport_data = [
        (1, 1, 1, 3, 2, 'pending', 'AI module crashes under heavy load.'),
        (2, 2, 1, 4, 3, 'resolved', 'Compilation errors in data preprocessing script.'),
        (3, 3, 2, 2, 5, 'pending', 'Missing command in the API endpoint for user authentication.'),
        (4, 4, 2, 5, 4, 'pending', 'Run time error when connecting to the database.'),
        (5, 5, 3, 3, 4, 'resolved', 'Communication problem between front-end and back-end services.'),
        (6, 6, 3, 5, 5, 'pending', 'Logical error in discount calculation function.'),
        (7, 7, 1, 3, 2, 'resolved', 'Inappropriate error handling in the user registration module.'),
        (8, 8, 2, 4, 5, 'pending', 'Calculation issue in the financial report generation.')
    ]

    assignproject_data = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5)
    ]

    # Insert data with error handling
    try:
        cursor.executemany('''INSERT INTO Employee (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', employee_data)
    except mysql.connector.IntegrityError as e:
        print(f"Error inserting Employee data: {e}")

    try:
        cursor.executemany('''INSERT INTO Project (projectID, projectName, SDate, EDate, projectDec) VALUES (%s, %s, %s, %s, %s)''', project_data)
    except mysql.connector.IntegrityError as e:
        print(f"Error inserting Project data: {e}")

    try:
        cursor.executemany('''INSERT INTO BugType (bugCode, bugCategory, bugSeverity) VALUES (%s, %s, %s)''', bugtype_data)
    except mysql.connector.IntegrityError as e:
        print(f"Error inserting BugType data: {e}")

    try:
        cursor.executemany('''INSERT INTO BugReport (bugNo, bugCode, projectID, TCode, ECode, status, bugDes) VALUES (%s, %s, %s, %s, %s, %s, %s)''', bugreport_data)
    except mysql.connector.IntegrityError as e:
        print(f"Error inserting BugReport data: {e}")

    try:
        cursor.executemany('''INSERT INTO AssignProject (projectID, empCode) VALUES (%s, %s)''', assignproject_data)
    except mysql.connector.IntegrityError as e:
        print(f"Error inserting AssignProject data: {e}")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
