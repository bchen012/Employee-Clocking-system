Instructions for running the code:
1. run the following in command line: pip install pandas
2. open project in your IDE (e.g Spyder, Visual studio code, or pycharm)
3. run the main.py file





Objective: Create an attendance and claims system for the HR department to achieve the following aims:
	•	Track employee’s working hours (aim: make it easier for HR to calculate payroll)
	•	Track which employee arrived late to work (aim: make it easier for HR to deduct late employees’ pay from payroll)
	•	Automate claims application for employee who are working overtime (in other words, only employees who are working overtime i.e. clock out after 6pm, are entitled to claims application. Aim: automate the claims application process)
	•	Track the overtime hours worked by employees (According to the Ministry of Manpower, if an employee works for more than 12 hours a day without applying for a special pass, it is a criminal offence. Hence, our aim here is to flag out the names of employees who have worked more than 12 hours to the HR department)

Assuming that the company has only 5 employees:
	•	Lim Shi Xuan Ivy 	(employee id: 1001)
	•	Wee Shi Yuan 	(employee id: 1002)
	•	Ng Teng Han 		(employee id: 1003)
	•	Liew Shan Ling 	(employee id: 1004)
	•	Liew Jing Yi Valarie 	(employee id: 1005)

Assume daily working hours for employees as 9am to 6pm.
The user manual for employees is: 
menu = ''' 
    1. Clock In
    2. Clock Out
    3. Daily Attendance Record
    4. Apply Claims
    X. Exit
    '''

For every option chosen except for “X”, employees will have to first log with their employee ID. 

Option 1: Clock In - Employees will be asked to log in + input temperature records + record current date and time

Option 2: Clock Out - Employees will be asked to log in + record current date and time

Option 3: Daily Attendance Record - For HR to see at a glance who is late, working OT, or absent on which date or day.

Option 4: Claims Application - Employees who timed out after 6pm will be entitled to meal claim (fixed $7) and transport claims (Variable - up to employee to input). Employees who timed out before or at 6pm will not be entitled to submit any claims. 

Note: Claims and Daily Attendance Record should link together - e.g. if the employee makes a claim on 29th March, then his clock out hours should be after 6pm. Otherwise, the claim is a fraud. 

Before employees can make a claim, insert a command to read the attendance.csv file to ensure that their Time Out time is after 6pm. Otherwise, the employee will not be eligible to make any claim. 

