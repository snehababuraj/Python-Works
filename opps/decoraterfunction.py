#decorater function is normal function
#decorater function has an inner function
#wrapper function has same number of parameters as decorater function n1,n2
#wrapper call div,sub
#wrapper is called by the outer function swap_dec()
def swap_dec(fn):

    def wrapper(n1,n2):
        if(n1<n2):
            (n1,n2)=(n2,n1)
            return fn(n1,n2)
        else:
            return fn(n1,n2)
    return wrapper


@swap_dec
def sub(n1,n2):
    return(n1-n2)
print(sub(20
          ,10))