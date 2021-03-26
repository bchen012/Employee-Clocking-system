import pandas as pd
import json
from datetime import datetime, date, time, timedelta


class EmployeeMgr:
    def __init__(self):
        self.employees = pd.read_csv('employee_data.csv')       #loads all the employee data into system
        # print(self.employees)
        self.attendance_and_claims_data = pd.read_csv('attendance_and_claims.csv')

        self.attendanceData = {}
        with open('attendance.txt','r') as inf:
            self.attendanceData = eval(inf.read())      #loads all the attendance data into system


    def check_employee_id(self, id):    #returns true if employee id exists and false if not
        if len(self.employees.loc[self.employees['Employee ID'] == id].values)>0:
            return True
        return False


    def get_employee_name(self, id):
        employeeName = self.employees.loc[self.employees['Employee ID'] == id, 'Employee Name'].values[0]
        return employeeName


    def update_employee_name(self, id):
        print("Current name is " + self.get_employee_name(id) + ".")
        newName = input("Please enter your new name: ")
        self.employees.loc[self.employees['Employee ID'] == id, 'Employee Name'] = newName
        print("Name has been updated to " + newName)

    def get_employee_attendance_data(self, id):
        return self.attendanceData[id]


    def clock_in_employee(self, id):
        clockedIn = self.employees.loc[self.employees['Employee ID'] == id, 'Clocked In'].values[0]
        if clockedIn == 'yes':
            print("Employee already clocked in.")
            return

        temperature = float(input("Please enter your temperature: "))
        if temperature > 37.5: 
            print("Entry denied. You are having a fever, please go and see a doctor! ")
            return

        self.employees.loc[self.employees['Employee ID'] == id, 'Clocked In'] = 'yes'    #update employees clock in status

        # current = datetime.now()
        #current.strftime("%d/%m/%y")
        #current.strftime("%H:%M")
        month = input("Enter current month: ") 
        date = input("Enter current date: ")
        clockInTime = input("Enter current time (Example - 1730): ")

        clockInDate = "2021/" + month + "/" + date
        

        if id not in self.attendanceData:       #update the attendance data
            self.attendanceData[id] = [clockInDate + ' ' + clockInTime]
        else:
            self.attendanceData[id].append(clockInDate + ' ' + clockInTime)

        clockInRecord = self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Clock In Record'].values[0]
        print(clockInRecord)
        # clockInRecord = clockInRecord + clockInDate + ' ' + clockInTime + ','
        self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Clock In Record'] = clockInRecord
        
        employeeName = self.get_employee_name(id)
        print(employeeName, "clocked in. Date: " + clockInDate + "  time: " + clockInTime)
        if int(clockInTime) > 900:
            print("You are late! \n")


    def clock_out_employee(self, id):
        clockedIn = self.employees.loc[self.employees['Employee ID'] == id, 'Clocked In'].values[0]
        if clockedIn == 'no':
            print("Employee is not clocked in.")
            return

        self.employees.loc[self.employees['Employee ID'] == id, 'Clocked In'] = 'no'    #update employees clock in status

        # current = datetime.now()
        # date_now = current.strftime("%d/%m/%y")
        # time_now = current.strftime("%H:%M")

        month = input("Enter current month: ") 
        date = input("Enter current date: ")
        clockOutTime = input("Enter current time (Example - 1730): ")
        clockOutDate = "2021/" + month + "/" + date

        if id not in self.attendanceData:       #update the attendance data
            self.attendanceData[id] = [clockOutDate + ' ' + clockOutTime]
        else:
            self.attendanceData[id].append(clockOutDate + ' ' + clockOutTime)

        clockOutRecord = self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Clock Out Record'].values[0]
        clockOutRecord = clockInRecord + clockOutDate + ' ' + clockOutTime + ','
        self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Clock Out Record'] = clockOutRecord
        
        employeeName = self.get_employee_name(id)
        print(employeeName, "clocked out. Date: " + clockOutDate + "  time: " + clockOutTime)
        if int(clockOutTime) > 1700:
            self.employees.loc[self.employees['Employee ID'] == id, 'Claim'] = clockOutDate


    def apply_claim(self, id):
        if self.employees.loc[self.employees['Employee ID'] == id, 'Claim'].values[0] != "None":
            claimAmount = input("Please enter the amount you would like to claim: ")
            reply = input("Are you sure that you want to submit $" + claimAmount + " for transport claim? (Y/N)")
            if reply == 'Y':
                print("Your claim for $" + claimAmount + " has been submitted. Please pass your receipts to the HR dept for further processing.")
                self.employees.loc[self.employees['Employee ID'] == id, 'Claim'] = "None"
            else:
                print("Claim application abortted.")
        else:
            print("You have no claims available.")


    def register_employee(self, name, id):
        values_to_add = pd.DataFrame({'Employee ID': [id], 'Employee Name': [name], 'Clocked In': ["no"], 'Claim': ['None']})
        # print(values_to_add)
        self.employees = self.employees.append(values_to_add, ignore_index = True)

        values_to_add = pd.DataFrame({'Employee ID': [id],'Clock In Record': [''],'Clock Out Record': [''],'Claims Record':['']})
        self.attendance_and_claims_data = self.attendance_and_claims_data.append(values_to_add, ignore_index = True)
        # print(self.employees)
        print(name + " (" + id + ") has been added as a new employee. Welcome!")


    def save_data_to_files(self):
        f = open("attendance.txt","w")
        f.write( str(self.attendanceData) )
        f.close()
        self.employees.to_csv("employee_data.csv", index=False)
        self.attendance_and_claims_data.to_csv("attendance_and_claims.csv", index=False)

        
    