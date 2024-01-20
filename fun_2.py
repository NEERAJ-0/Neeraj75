def fact():
    n=int(input('Enter a number:'))
    out=1
    for i in range(1,n+1):
        out*=i
    print(out)
fact()