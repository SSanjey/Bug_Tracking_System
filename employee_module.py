import mysql.connector

class Employee:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sanjey123@",
            database="BDS",
            port=3306
        )
        self.cursor = self.conn.cursor()

    def update_profile(self, empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role):
        self.cursor.execute('''UPDATE Employee SET empName = %s, empEmail = %s, empPassword = %s, gender = %s, DOB = %s, mobileNo = %s, Role = %s
                               WHERE empCode = %s''', 
                               (empName, empEmail, empPassword, gender, DOB, mobileNo, Role, empCode))
        self.conn.commit()

    def add_bug_report(self, bugNo, bugCode, projectID, TCode, ECode, status, bugDes):
        self.cursor.execute('''INSERT INTO BugReport (bugNo, bugCode, projectID, TCode, ECode, status, bugDes)
                               VALUES (%s, %s, %s, %s, %s, %s, %s)''', 
                               (bugNo, bugCode, projectID, TCode, ECode, status, bugDes))
        self.conn.commit()

    def update_bug_status(self, bugNo, status):
        self.cursor.execute('''UPDATE BugReport SET status = %s WHERE bugNo = %s''', 
                               (status, bugNo))
        self.conn.commit()

    def view_bugs(self):
        self.cursor.execute('''SELECT * FROM BugReport''')
        return self.cursor.fetchall()

    def bug_details(self, bugNo):
        self.cursor.execute('''SELECT * FROM BugReport WHERE bugNo = %s''', (bugNo,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()
