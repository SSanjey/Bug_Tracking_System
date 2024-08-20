import mysql.connector

class Admin:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sanjey123@",
            database="BDS",
            port=3306
        )
        self.cursor = self.conn.cursor()

    def add_manager(self, empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role):
        self.cursor.execute('''INSERT INTO Employee (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', 
                               (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role))
        self.conn.commit()

    def view_manager(self):
        self.cursor.execute('''SELECT * FROM Employee WHERE Role = "manager"''')
        return self.cursor.fetchall()

    def delete_manager(self, empCode):
        self.cursor.execute('''DELETE FROM Employee WHERE empCode = %s AND Role = "manager"''', (empCode,))
        self.conn.commit()

    def update_manager(self, empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role):
        self.cursor.execute('''UPDATE Employee SET empName = %s, empEmail = %s, empPassword = %s, gender = %s, DOB = %s, mobileNo = %s, Role = %s
                               WHERE empCode = %s AND Role = "manager"''', 
                               (empName, empEmail, empPassword, gender, DOB, mobileNo, Role, empCode))
        self.conn.commit()

    def add_employee(self, empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role):
        self.cursor.execute('''INSERT INTO Employee (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', 
                               (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role))
        self.conn.commit()

    def view_employee(self):
        self.cursor.execute('''SELECT * FROM Employee WHERE Role != "manager"''')
        return self.cursor.fetchall()

    def delete_employee(self, empCode):
        self.cursor.execute('''DELETE FROM Employee WHERE empCode = %s AND Role != "manager"''', (empCode,))
        self.conn.commit()

    def update_employee(self, empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role):
        self.cursor.execute('''UPDATE Employee SET empName = %s, empEmail = %s, empPassword = %s, gender = %s, DOB = %s, mobileNo = %s, Role = %s
                               WHERE empCode = %s AND Role != "manager"''', 
                               (empName, empEmail, empPassword, gender, DOB, mobileNo, Role, empCode))
        self.conn.commit()

    def view_all_projects(self):
        self.cursor.execute('''SELECT * FROM Project''')
        return self.cursor.fetchall()

    def view_bug_reports(self):
        self.cursor.execute('''SELECT * FROM BugReport''')
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
