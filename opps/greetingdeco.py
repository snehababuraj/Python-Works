def greeting_dec(fn):
    def wrapper(name):
        result=fn(name)
        return f"hello coder{result}"
    return wrapper

@greeting_dec
def morning_greeting(name):
    return f"{name}Good Morning"
@greeting_dec
def afternoon_greeting(name):
    return f"{name}Good afternoon"
@greeting_dec
def evening_greeting(name):
    return f"{name}Good evening"
print(morning_greeting("sai"))
print(afternoon_greeting("vipin"))