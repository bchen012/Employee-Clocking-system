
employee_id = ["1001", "1002", "1003", "1004", "1005"]
employee_name = ["Lim Shi Xuan Ivy", "Wee Shi Yuan", "Ng Teng Han", "Liew Shan Ling", "Liew Jing Yi Valarie"]
employee_id_and_name = {}
employee_id_and_name['1001'] = "Lim Shi Xuan Ivy"
employee_id_and_name['1002'] = "Wee Shi Yuan"
employee_id_and_name['1003'] = "Ng Teng Han"
employee_id_and_name['1004'] = "Liew Shan Ling"
employee_id_and_name['1005'] = "Liew Jing Yi Valerie"


import csv
from datetime import datetime, date, time, timedelta
moment = datetime.now()


# Step 1
# create a time_in record with these columns - employee ID, employee Name, Date, Time in, Time Out, No. of Hours Worked
# Problem: how can we print "done" instead of "none"?
def create_attendance_record():
    import csv
    row = ["Employee ID", "Employee Name", "Date", "Time In", "Temperature", "Time Out", "No. of Hours Worked"]
    with open("attendance.csv", "w") as file_pointer:
        csv_pointer = csv.writer(file_pointer)
        csv_pointer.writerow(row)
        print("Done")


# step 2
# allow employees to clock in their timing and temperature when they reach the workplace
def clock_in(): 
    
    employee_id = ["1001", "1002", "1003", "1004", "1005"]
    employee_name = ["Lim Shi Xuan Ivy", "Wee Shi Yuan", "Ng Teng Han", "Liew Shan Ling", "Liew Jing Yi Valarie"]
    employee_id_and_name = {}
    employee_id_and_name['1001'] = "Lim Shi Xuan Ivy"
    employee_id_and_name['1002'] = "Wee Shi Yuan"
    employee_id_and_name['1003'] = "Ng Teng Han"
    employee_id_and_name['1004'] = "Liew Shan Ling"
    employee_id_and_name['1005'] = "Liew Jing Yi Valerie"
    
    current = datetime.now()
    date_now = current.strftime("%d/%m/%y")
    time_now = current.strftime("%H:%M")

    employee_id_check = input("Hello, please input your employee id: ").strip()
        
    for each in employee_id:
        if employee_id_check == each:
            print("hello, ", employee_id_and_name[employee_id_check])
            temperature = float(input("Welcome, please enter your temperature: ").strip())
            if temperature < 37.6:
                with open("attendance.csv", "a", newline = "") as clockin:
                    csv_pointer = csv.writer(clockin)
                    csv_pointer.writerow([employee_id_check, employee_id_and_name[employee_id_check], date_now, str(time_now), str(temperature)])
                        
            elif temperature > 37.5: 
                print("Entry denied. You are having a fever, please go and see a doctor! ")
                
            else:
                print("")           

# check which employee arrive late to work 
# aim: to read each row in time_in.csv and flag out employees who are late i.e. time_in after 9:15 am
# this function is not working
def late_checker(): 
       
    import csv
    
    with open('attendance.csv', 'r') as read_obj:
        late_record_checker = csv.reader(read_obj)
        
        next(late_record_checker)
        
        for each_line in late_record_checker:
            x = print(each_line[3])
            if str(x) < "09:16":
                print("hello, ", each_line([1]), "is on time")
            
            else:
                print("hello, ", each_line([1]), "you are late")


# aim: allow employees to record their clock out timing
# problem: how do I insert content into speciifc rows in attendance.csv? i.e. I ony want to input clock out timing under the clock out column in attendance.csv 
# problem: how can i allow my code to have to match the time out records to the correct employee name?
def clock_out():
    current = datetime.now()
    date_now = current.strftime("%d/%m/%y")
    time_now = current.strftime("%H:%M")
    
    employee_id_check = input("Hello, please input your employee id: ").strip()
    print("Invalid id. Try again! ")
    employee_id_check = input("Hello, please input your employee id: ").strip()
        
    for each in employee_id:
        if employee_id_check == each:
            with open("attendance.csv", "a", newline = "") as clockout:
                csv_pointer = csv.writer(clockout)
                
                print("Goodbye, ", employee_id_and_name[employee_id_check])
                

# def daily_attendance_record(): # not created yet
    
    
# def claims(): # not created yet
    


menu = ''' 
    1 Clock In
    2 Clock Out
    3 View Daily Attendance Record
    4 Claims
    X Exit
    '''

print(create_attendance_record())
while True:
    print(menu)

choice = input("Please select what do you want to do").upper().strip()
if choice == "X":
    break
    
elif choice == "1":
       print(clock_in()) 
       
elif choice == "2":
        print(clock_out)
        
elif choice == "3": # problem: daily attendance record is not created yet as we encountered initial problems with our clock out function

elif choice == "4":
    meal_claim = 0
    transport_claim = 0

    filename = "claims.csv"
    employee_id = ["1001", "1002", "1003", "1004", "1005"]
    employee_name = ["lim shi xuan ivy", "wee shi yuan", "ng teng han", "liew shan ling", "liew jing yi valerie"]
    employee_id_and_name = {}
    employee_id_and_name['1001'] = "lim shi xuan ivy"
    employee_id_and_name['1002'] = "wee shi yuan"
    employee_id_and_name['1003'] = "ng teng han"
    employee_id_and_name['1004'] = "liew shan ling"
    employee_id_and_name['1005'] = "liew jing yi valerie"

    import csv

    employee_id_check = input("Hello, please enter your employee ID: ")
        for each in employee_id:
            if employee_id_check == each:
                print("hello, ", employee_id_and_name[employee_id_check])
                menu2 = '''
                1. Meal
                2. Transport
                X. Exit
                '''
                while True:
                    print(menu2)
                    try:
                        choice_claim = input("Please select an option: ").upper()
                        if choice_claim == 'X':
                            break
                        elif choice_claim == '1':
                            meal_claim += 7
                            print("Total claimable amount for meals: $", meal_claim) 
                        elif choice_claim == '2':
                            transport_claim = input("Please input the amount you wish to claim for transportation: $")
                            print("Total claimable amount for transportion: $",transport_claim)
                        else:
                            print("Invalid selection") 
                        
                        Z = int(transport_claim) + int(meal_claim)
                        with open(filename, 'a', newline = "") as file_pointer:
                            csv_pointer = csv.writer(file_pointer)
                            row = [employee_id_check, employee_id_and_name[employee_id_check], meal_claim, transport_claim]
                            csv_pointer.writerow(row)
                            print("The total amount you wish to claim is: $", Z)
                            print("We have received your request and will be processing it shortly. Do also kindly submit your transportation receipts to the Finance Department for audit purposes. Thank you")
                    
                    except ValueError:
                        print("Invalid selection")
            
                
                

        
       
     
        
    



