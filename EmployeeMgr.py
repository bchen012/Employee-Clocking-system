import pandas as pd
import json
from datetime import datetime, date, time, timedelta


class EmployeeMgr:
    def __init__(self):
        self.employees = pd.read_csv('employee_data.csv')       #loads all the employee data into system
        # print(self.employees)

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

        current = datetime.now()
        date_now = current.strftime("%d/%m/%y")
        time_now = current.strftime("%H:%M")

        if id not in self.attendanceData:       #update the attendance data
            self.attendanceData[id] = [date_now + ' ' + time_now]
        else:
            self.attendanceData[id].append(date_now + ' ' + time_now)
        
        employeeName = self.get_employee_name(id)
        print(employeeName, "clocked in. Date: " + date_now + "  time: " + time_now)


    def clock_out_employee(self, id):
        clockedIn = self.employees.loc[self.employees['Employee ID'] == id, 'Clocked In'].values[0]
        if clockedIn == 'no':
            print("Employee is not clocked in.")
            return

        self.employees.loc[self.employees['Employee ID'] == id, 'Clocked In'] = 'no'    #update employees clock in status

        current = datetime.now()
        date_now = current.strftime("%d/%m/%y")
        time_now = current.strftime("%H:%M")

        if id not in self.attendanceData:       #update the attendance data
            self.attendanceData[id] = [date_now + ' ' + time_now]
        else:
            self.attendanceData[id].append(date_now + ' ' + time_now)
        
        employeeName = self.get_employee_name(id)
        print(employeeName, "clocked out. Date: " + date_now + "  time: " + time_now)


    def register_employee(self, name, id):
        values_to_add = pd.DataFrame({'Employee ID': [id], 'Employee Name': [name], 'Clocked In': ["no"]})
        print(values_to_add)
        self.employees = self.employees.append(values_to_add, ignore_index = True)
        print(self.employees)
        print(name + " (" + id + ") has been added as a new employee. Welcome!")


    def save_data_to_files(self):
        f = open("attendance.txt","w")
        f.write( str(self.attendanceData) )
        f.close()
        self.employees.to_csv("employee_data.csv", index=False)

        
    