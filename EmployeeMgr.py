import pandas as pd
import json
from datetime import datetime, date, time, timedelta
from input_util import get_input_range


class EmployeeMgr:
    def __init__(self):
        self.employees = pd.read_csv('employee_data.csv')       #loads all the employee data into system
        self.attendance_and_claims_data = pd.read_csv('attendance_and_claims.csv')

        # self.attendanceData = {}
        # with open('attendance.txt','r') as inf:
        #     self.attendanceData = eval(inf.read())      #loads all the attendance data into system


    def check_employee_id(self, id):    #returns true if employee id exists and false if not
        return id in self.employees['Employee ID'].values


    def get_employee_name(self, id):
        employeeName = self.employees.loc[self.employees['Employee ID'] == id, 'Employee Name'].values[0]
        return employeeName


    def update_employee_name(self, id):
        print("Current name is " + self.get_employee_name(id) + ".")
        newName = input("Please enter your new name: ")
        self.employees.loc[self.employees['Employee ID'] == id, 'Employee Name'] = newName
        print("Name has been updated to " + newName)

    def get_employee_attendance_data(self, id):
        clockInData = self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Clock In Record'].values[0]
        clockOutData = self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Clock Out Record'].values[0]
        clockInList = clockInData.split(',')
        clockOutList = clockOutData.split(',')
        attendanceList = []
        for i in range(len(clockOutList)-1):
            attendanceList.append(clockInList[i])
            attendanceList.append(clockOutList[i])
        return attendanceList


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
        month = get_input_range("Enter current month: ", 1, 12)
        date = get_input_range("Enter current date: ", 1, 31)
        clockInTime = input("Enter current time (Example - 1730): ")

        clockInDate = "2021/" + month + "/" + date

        clockInRecord = self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Clock In Record'].values[0]
        if clockInRecord == 'None':
            clockInRecord = clockInDate + ' ' + clockInTime + ','
        else:
            clockInRecord = clockInRecord + clockInDate + ' ' + clockInTime + ','
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

        month = get_input_range("Enter current month: ", 1, 12)
        date = get_input_range("Enter current date: ", 1, 31)
        clockOutTime = input("Enter current time (Example - 1730): ")
        clockOutDate = "2021/" + month + "/" + date

        clockOutRecord = self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Clock Out Record'].values[0]
        if clockOutRecord == 'None':
            clockOutRecord = clockOutDate + ' ' + clockOutTime + ','  
        else:          
            clockOutRecord = clockOutRecord + clockOutDate + ' ' + clockOutTime + ','
        self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Clock Out Record'] = clockOutRecord
        
        employeeName = self.get_employee_name(id)
        print(employeeName, "clocked out. Date: " + clockOutDate + "  time: " + clockOutTime)
        if int(clockOutTime) > 1700:
            self.employees.loc[self.employees['Employee ID'] == id, 'Claim'] = clockOutDate


    def apply_claim(self, id):
        dateOfClaim = self.employees.loc[self.employees['Employee ID'] == id, 'Claim'].values[0]
        if dateOfClaim != "None":
            claimAmount = input("Please enter the amount you would like to claim: ")
            reply = input("Are you sure that you want to submit $" + claimAmount + " for transport claim? (Y/N)")
            if reply == 'Y':
                claimRecord = self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Claims Record'].values[0]
                if claimRecord == 'None':
                    claimRecord = '$' + claimAmount + ' for OT on ' + dateOfClaim + ','
                else:
                    claimRecord = claimRecord + '$' + claimAmount + ' for OT on ' + dateOfClaim + ','
                self.attendance_and_claims_data.loc[self.attendance_and_claims_data['Employee ID'] == id, 'Claims Record'] = claimRecord
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

        values_to_add = pd.DataFrame({'Employee ID': [id],'Clock In Record': ['None'],'Clock Out Record': ['None'],'Claims Record':['None']})
        self.attendance_and_claims_data = self.attendance_and_claims_data.append(values_to_add, ignore_index = True)
        # print(self.employees)
        print(name + " (" + str(id) + ") has been added as a new employee. Welcome!")


    def save_data_to_files(self):
        # f = open("attendance.txt","w")
        # f.write( str(self.attendanceData) )
        # f.close()
        self.employees.to_csv("employee_data.csv", index=False)
        self.attendance_and_claims_data.to_csv("attendance_and_claims.csv", index=False)

        
    