import re

file = open(r"C:\Users\administrator.MCA\Desktop\republic.txt",'r')
data=file.read()
out = re.sub(' ','_',data)
file=open(r"C:\Users\administrator.MCA\Desktop\republic.txt",'w')
file.write(out)
file.close()

# (or) with open(r"C:\Users\administrator.MCA\Desktop\republic.txt",'r',encoding='utg-8') as file:
    #     data = file.read()
    #     new=re.sub(' ','_',data)
    #     file.seek(0)
    #     file.wite(new)


