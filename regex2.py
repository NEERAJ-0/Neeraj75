import re

#Mobileno
print(re.findall('\+91\- ?[6-9][0-9]{9}','+91-8974561230,4565884654,5555454574,+91- 7899585635'))

#PAN.No
print(re.findall('[A-Z]{5}[0-9]{4}[A-Z]','ABCDE1234F,45GJWGHUH'))

#AP vehical No
#for space '[ ]' or ' ' or \s
print(re.findall('AP[ ]?[0-3][1-9]{2}[ ]?[a-zA-Z][ ]?[0-9]{4}','AP 05 n 5302'))
print(re.findall('AP ?[0-3][1-9]{2} ?[a-zA-Z] ?[0-9]{4}','AP 05 n 5302'))
print(re.findall('AP\s?[0-3][1-9]{2}\s?[a-zA-Z]\s?[0-9]{4}','AP 05 n 5302'))

#email
print(re.findall('[a-zA-Z0-9]+\.?[a-zA-Z0-9]*\@gmail\.com','abcd123.@gmail.com'))

