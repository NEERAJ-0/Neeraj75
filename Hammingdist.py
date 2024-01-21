def hamming(s1,s2):              #def fun(a,b,out=0)
    if len(s1)==len(s2):
        out=0
        for i in range(len(s1)): #for i,j in zip(a,b):
            if s1[i]!=s2[i]:     #if i!=j:
                out+=1
        return out
    return 'string length not same'
print(hamming('abcde','bcade'))
