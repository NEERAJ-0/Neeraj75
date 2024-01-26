import re

with open(r"C:\Users\administrator.MCA\Desktop\context.txt",'r') as file:

    data = file.read()
    out  = re.findall('[aeiouAEIOU]',data)
    print(len(out))
    file.close()