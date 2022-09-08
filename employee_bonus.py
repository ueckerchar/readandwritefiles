import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)

for record in csvfile:
    
    ID = record[0]
    first_name = record[1]
    last_name = record[2]
    salary = float(record[3])
    bonus = float(record[4])
    total_pay = salary + (salary*bonus)

    print("ID: ", ID)
    print("Full Name: ", first_name, last_name)
    print("Salary: ","$", salary)
    print("Bonus: ", bonus)
    print("Total Pay: ", "$", total_pay)

    input()

infile.close()