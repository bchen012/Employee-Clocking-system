import pandas as pd
import json
from datetime import datetime, date, time, timedelta

#df.loc[df['column_name'] == some_value]

class EmployeeMgr:
    def __init__(self):
        self.employees = pd.read_csv('employee_data.csv')       #loads all the employee data into system
        print(self.employees)

        self.attendanceData = {}
        with open('attendance.txt','r') as inf:
            self.attendanceData = eval(inf.read())      #loads all the attendance data into system


    def check_employee_id(self, id):    #returns true if employee id exists and false if not
        if len(self.employees.loc[self.employees['Employee ID'] == id])>0:
            return True
        return False


    def get_employee_name(self, id):
        employeeRows = self.employees.loc[self.employees['Employee ID'] == id]
        return employeeRows['Employee Name'][0]


    def clock_in_employee(self, id): 
        row = self.employees.loc[self.employees['Employee ID'] == id]
        if row['Clocked In'][0] == 'yes':
            print("Employee already clocked in.")
            return

        self.employees.loc[self.employees['Employee ID'] == id, 'Clocked In'] = 'yes'    #update employees clock in status

        current = datetime.now()
        date_now = current.strftime("%d/%m/%y")
        time_now = current.strftime("%H:%M")

        if id not in self.attendanceData:
            self.attendanceData[id] = [date_now + ' ' + time_now]
        else:
            self.attendanceData[id].append([date_now + ' ' + time_now])
        
        print(date_now, time_now)


    def register_employee(self, name, id):
        values_to_add = pd.DataFrame({'Employee ID': [id], 'Employee Name': [name], 'Clocked In': ["no"]})
        print(values_to_add)
        self.employees = self.employees.append(values_to_add, ignore_index = True)
        print(self.employees)
        print(name + " (" + id + ") has been added as a new employee. Welcome!")


    def save_date_to_files(self):
        f = open("attendance.txt","w")
        f.write( str(self.attendanceData) )
        f.close()
        self.employees.to_csv("employee_data.csv", index=False)

        