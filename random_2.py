import random
i=1
otp=''
while i<=6:
    otp+=str(random.randint(0,9))
    i+=1
print(otp)
    
    