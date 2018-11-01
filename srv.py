
def hello(str):
    return 'I am copied Uday '+str

def doRun(*args,**kwargs):
    print(args)
    print(kwargs)

if(__name__=='__main__'):
    obj={'hello':'world','name':'uday'}

    doRun(obj)