import time
def duration(fun):
    def inner():
        start=time.time()
        fun()
        end = time.time()
        print(f'The total time taken to answer them question is {end - start}secs')
    return inner

@duration
def question1():
    print('who is the prime minister of india')
    respone=input('enter your respone:')

@duration
def question2():
    print('who is the principal of mca')
    respone=input('enter your respone:')

@duration
def question2():
    print('who is the capital of AP')
    respone=input('enter your respone:')