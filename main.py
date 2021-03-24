from EmployeeMgr import EmployeeMgr
from Attendance_Record import print_Attendance
import pandas as pd


employeeMgr = EmployeeMgr()     #initialize the employee manager

choice1 = int(input("Please choose an option: \n1. Login \n2. Register \n3. Exit\n"))
while choice1 <= 2:
    if choice1 == 1:
        employeeID = int(input("Enter your employee ID: "))
        if employeeMgr.check_employee_id(employeeID):
            print("Hi " + employeeMgr.get_employee_name(employeeID))

            choice2 = int(input("Please choose an option: \n1. Clock In \n2. Clock Out \n3. Daily Attendance Record \n4. Apply Claims \n5. Update Name \n6. Exit\n"))
            while choice2 <= 5:
                if choice2 == 1:
                    employeeMgr.clock_in_employee(employeeID)
                elif choice2 == 2:
                    employeeMgr.clock_out_employee(employeeID)
                elif choice2 == 3:
                    print_Attendance(employeeMgr.get_employee_attendance_data(employeeID))
                elif choice2 == 4:
                    employeeMgr.apply_claim(employeeID)
                elif choice2 == 5:
                    employeeMgr.update_employee_name(employeeID)


                choice2 = int(input("Please choose an option: \n1. Clock In \n2. Clock Out \n3. Daily Attendance Record \n4. Apply Claims \n5. Update Name \n6. Exit\n"))
    
    elif choice1 == 2:
        newEmployeeName = input("Enter an name: ")
        newEmployeeID = input("Enter an ID: ")
        employeeMgr.register_employee(newEmployeeName, newEmployeeID)

    choice1 = int(input("Please choose an option: \n1. Login \n2. Register \n3. Exit\n"))

employeeMgr.save_data_to_files()    #save the data to attendance.txt and employee_data