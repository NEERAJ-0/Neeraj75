import cx_Oracle
import csv
conn=cx_Oracle.Connection('system/manager@mother')
cr=conn.cursor()

def createtable():
    query='''create table neeraj75(
        id number(2) primary key,
        name varchar(50)
    )'''
    cr.execute(query)
#createtable()

def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    cr.execute("insert into neeraj75(id,name)  values(:id,:name)",record)
    conn.commit()
#insertrecord()

def read_record():
    query='select * from neeraj75'
    cr.execute(query)
    record = cr.fetchall()
    for row in record:
        print(row)
#read_record()

def read_record():
    query='select * from neeraj75'
    cr.execute(query)
    record = cr.fetchall()
    with open('record.csv','w',newline='') as csvfile:
        data=csv.writer(csvfile)
        data.writerow(['id','name'])
        for row in record:
            data.writerow(row)

def insertdata():
    with open('record.csv','r',newline='') as file:
        data=csv.reader(csvfile)
        data= list(data)
        for row in range(1,len(data)):
            insertrecord(*data[row])
        # record=csv.DictReader(file)
        # for i in record:
        #     cr.execute("insert into neeraj75(id,name)  values(:id,:name)",i)
        #     conn.commit()
insertdata()



# def updaterecord(sid,name):
#     record={'id':str(sid),'name':name}
#     cr.execute("update neeraj75 set name=(:name)  where id=(:id)",record)
#     conn.commit()
#updaterecord(2,'neeraj)

# def fetch_record(sid):
#     record={'id':str(sid)}
#     query = 'select * from neeraj75 where id=:id'
#     cr.execute(query,record)
#     record=cr.fetchall()
#     for row in record:
#         print(row)
#fetch_record()


# def updaterecord(sid):
#     fetch_record(sid)
#     name=input('enter new name to update: ')
#     record={'id':str(sid),'name':name}
#     query="update neeraj75 set name=(:name)  where id=:id"
#     cr.execute(query,record)
#     conn.commit()
#     fetch_record(sid)
#updaterecord()


# def deleterecord(sid):
#     record={'id':str(sid)}
#     cr.execute("delete from neeraj75 where id=:id",record)
#     conn.commit()
#deleterecord()

# def truncate():
#    query='truncate table neeraj75'
#    cr.execute(query)
# truncate()  

#def droptable()
#   .....