a=[1,0,True,'','str',[1,2,3],78,0.0]
#print([i for i in a if bool(i)])
print(list(filter(bool,a)))