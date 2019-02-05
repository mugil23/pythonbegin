def power(base,ex):
    if(ex==1):
        return(base)
    if(ex!=1):
        return(base*power(base,ex-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,ex))
