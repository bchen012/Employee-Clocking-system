from EmployeeMgr import EmployeeMgr
from Attendance_Record import print_Attendance
import pandas as pd
from input_util import get_input_range, get_integer_input


employeeMgr = EmployeeMgr()     #initialize the employee manager

choice1 = get_input_range("Please choose an option: \n1. Login \n2. Register \n3. Exit\n", "Invalid response, please select from the given options. \n", 1, 3)  # Force them to input a int between 1 and 3
while choice1 <= 2:
    if choice1 == 1:
        employeeID = get_integer_input("Enter your employee ID: ", "\nInvalid ID, please try again. \n")
        if employeeMgr.check_employee_id(employeeID):
            print("Hi " + employeeMgr.get_employee_name(employeeID) + "! \n")

            choice2 = get_input_range("Please choose an option: \n1. Clock In \n2. Clock Out \n3. Daily Attendance Record \n4. Apply Claims \n5. Update Name \n6. Exit\n", 
                                      "Invalid response, please select from the given options", 1, 6)   # Force them to input a int between 1 and 6
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


                choice2 = get_input_range("Please choose an option: \n1. Clock In \n2. Clock Out \n3. Daily Attendance Record \n4. Apply Claims \n5. Update Name \n6. Exit\n", 
                                          "Invalid response, please select from the given options", 1, 6)

        else:
            print("Employee ID does not exist, please key in a valid ID.")

    elif choice1 == 2:
        newEmployeeName = input("Enter an name: ")
        newEmployeeID = get_input_range("Enter an ID: ", "Invalid employee ID, please try again. \n", 1000, 9999)   # Force them to input a int between 1000 and 9999
        while employeeMgr.check_employee_id(newEmployeeID):
            print("Employee ID alread in use. Please enter another one. \n")
            newEmployeeID = get_input_range("Enter an ID: ", "Invalid employee ID, please try again. \n", 1000, 9999)
        employeeMgr.register_employee(newEmployeeName, newEmployeeID)

    choice1 = get_input_range("Please choose an option: \n1. Login \n2. Register \n3. Exit\n", "Invalid response, please select from the given options. \n", 1, 3)

employeeMgr.save_data_to_files()    #save the data to attendance.txt and employee_data