import csv

infile = open('steps.csv','r')
outfile = open('avg_steps.csv','w')

csvfile = csv.reader(infile, delimiter = ',')

i = 0
x = 0

next(csvfile)

m = ['January','February','March','April','May','June','July','August','September','October','November','December']

month = 1

outfile.write('Month, Avg Steps\n')
for line in csvfile:
    print(i)
    if float(line[0]) != month:
        month = 1
        avg = (x/i)
        print(m[month]+', '+str(avg))
        outfile.write(m[month]+', '+str(avg)+'\n')
        month += 2
        i = 0
        x = 0


    outfile.close()