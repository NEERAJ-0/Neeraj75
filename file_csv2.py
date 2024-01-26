import csv

with open('sample2.csv','w',newline='') as csvfile:
    fieldnames=['id','name','age']
    record=csv.DictWriter(csvfile,fieldnames)
    record.writeheader()
    data=[
        {'id':1, 'name':'ram', 'age':20},
        {'id':2, 'name':'sita', 'age':18},
        {'id':3, 'name':'siri', 'age':10}
    ]
    record.writerows(data)

with open('sample2.csv','r',newline='') as file:
    record=csv.DictReader(file)
    for i in record:
        print(i)
