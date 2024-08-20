import mysql.connector

class Manager:
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

    def add_project(self, projectID, projectName, SDate, EDate, projectDec):
        self.cursor.execute('''INSERT INTO Project (projectID, projectName, SDate, EDate, projectDec)
                               VALUES (%s, %s, %s, %s, %s)''', 
                               (projectID, projectName, SDate, EDate, projectDec))
        self.conn.commit()

    def view_all_projects(self):
        self.cursor.execute('''SELECT * FROM Project''')
        return self.cursor.fetchall()

    def delete_project(self, projectID):
        self.cursor.execute('''DELETE FROM Project WHERE projectID = %s''', (projectID,))
        self.conn.commit()

    def update_project(self, projectID, projectName, SDate, EDate, projectDec):
        self.cursor.execute('''UPDATE Project SET projectName = %s, SDate = %s, EDate = %s, projectDec = %s
                               WHERE projectID = %s''', 
                               (projectName, SDate, EDate, projectDec, projectID))
        self.conn.commit()

    def add_bug(self, bugNo, bugCode, projectID, TCode, ECode, status, bugDes):
        self.cursor.execute('''INSERT INTO BugReport (bugNo, bugCode, projectID, TCode, ECode, status, bugDes)
                               VALUES (%s, %s, %s, %s, %s, %s, %s)''', 
                               (bugNo, bugCode, projectID, TCode, ECode, status, bugDes))
        self.conn.commit()

    def view_all_bugs(self):
        self.cursor.execute('''SELECT * FROM BugReport''')
        return self.cursor.fetchall()

    def update_bug(self, bugNo, status, bugDes):
        self.cursor.execute('''UPDATE BugReport SET status = %s, bugDes = %s WHERE bugNo = %s''', 
                               (status, bugDes, bugNo))
        self.conn.commit()

    def delete_bug(self, bugNo):
        self.cursor.execute('''DELETE FROM BugReport WHERE bugNo = %s''', (bugNo,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
