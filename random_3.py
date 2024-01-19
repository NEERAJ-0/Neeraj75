import random
captcha=[]
while len(captcha)<4    :
    captcha+=[random.choice(['!','@','#','$','&','?','*'])]
    captcha+=[str(random.randint(0,9))]
captcha+=[chr(random.randint(97,123))]
captcha+=[chr(random.randint(65,91))]
random.shuffle(captcha)
out=''
for i in captcha:
    out+=i
print(out)