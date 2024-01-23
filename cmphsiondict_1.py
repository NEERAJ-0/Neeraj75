a=[4,9,'abc',[1,2,3,4]]
print({i:a[i] for i in range(len(a))})
print({i:j for i,j in enumerate(a)})