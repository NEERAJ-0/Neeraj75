
try:
    a=10
    a=a/0
except (NameError,TypeError) as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
    print(20)
