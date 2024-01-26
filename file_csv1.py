import csv
#old syntax,  file = open('sample.csv','w')
with open('sample1.csv','w',newline='') as file:
    data=[
        [1,'neeraj',20],
        [2,'sundaresh',23],
        [3,'prasanth',19], 

        ]
    record = csv.writer(file)
    record.writerow(['id','name','age'])
    record.writerows(data)
    
#to get data from csv file
with open('sample1.csv','r',newline='') as file:
    record = csv.reader(file)
    for i in record:
        print(i)