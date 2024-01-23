a={'a':'abc',1:1234,'b':'bcde', 2:2345}
print({a[i]:i for i in a if type(i)==str })