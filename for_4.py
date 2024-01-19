a=[1,'1',2,2.4,[4,5,6],9,16,'abcd']
out=0
for s in a:
    if type(s)==int:
        if  s%2==0:
            out+=s
        else:
            out-=s
print(out)
'''a=[1,'1',2,2.4,[4,5,6],9,16,'abcd']
out=0
for s in a:
    if isinstance(s,int):
        if  s%2==0:
            out+=s
        else:
            out-=s        
print(out) '''

        

        
    
    

       
    

