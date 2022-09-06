

def main():
    import csv

    infile = open('customers.csv','r')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    for record in csvfile:
        print(record[1],'',record[2],',',record[4])

    outfile = open('customer_country.csv','w')


    outfile.write(csvfile)



main()
        

    