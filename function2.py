def cube(n):
    result=n**3
    return result
# print(cube(3))

def is_even(n):
    return True if n%2==0 else False 
# print(is_even(3))


def max_two(n1,n2): #snakecase
    return n1 if n1>n2 else n2
# print(max_two(10,3))


def last_digit_max_num(n1,n2):
    digit_n1=n1%10
    digit_n2=n2%10
    return n1 if digit_n1>digit_n2 else n2
# print(last_digit_max_num(257,480))


def nth_power(num,exp):
    return num**exp

    
# print(nth_power(10,3))


def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1
# print(smart_sub(3,5))


# def is_leapyr(yr) return true if year is leap year else return false

# def is_prime(num) return ture if num is prime else return false

# def is_armstrong (num) return true if num is amrstong else return false


def is_leapyr(year):
      if(year%100==0 and year%400==0) or( year%100!=0 and year%4==0):
          return True
      else:
          return False
# print(is_leapyr(2023))
          
def is_armstrong(num):
    digit_count=len(str(num))
    result=0
    org=num
    while(num!=0):
        digit=num%10
        exp=digit**digit_count
        result=result+exp
        num=num//10
    return org==result
# print(is_armstrong(151))
    

