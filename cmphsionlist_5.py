a=[9,'9',10,[1,3],'234',21,22.5]
print([(i,a[i]) for i in range(len(a)) if type(a[i])==int ])
print([(i,a[i]) for i in range(len(a)) if isinstance(a[i],int) ])