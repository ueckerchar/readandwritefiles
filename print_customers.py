import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile)


for record in csvfile:
    print('ID: ',record[0])
    print('Fname: ',record[1])
    print('Lname: ',record[2])
    print('City: ',record[3])
    print('Country: ',record[4])
    print('Phone: ',record[5])

    input()




