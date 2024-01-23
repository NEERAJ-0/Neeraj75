a='xyz'
b=[1,2,3]
print({a[i]:b[i] for i in range(len(a)) })
#or
print({i:j for i,j in zip(a,b)})