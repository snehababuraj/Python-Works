# there is no need of def and funcation name in lambda function,instead add keyword lambda
# syntax: variable_name=lambda parameters:function
            #  function definition

addition=lambda n1,n2:n1+n2
# print(addition(100,200))

subtraction=lambda n1,n2:n1
# print(subtraction(200,100))

is_even=lambda n: True if n %2==0 else False
# print(is_even(3))

cube=lambda n:n**3
# print(cube(2))

last_digit_max_num=lambda n1,n2:n1 if n1%10>n2%10 else n2
# print(last_digit_max_num(125,532))


nth_power=lambda num,exp:num**exp
# print(nth_power(10,2))


# is_leapyr=lambda year:True if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0) else False
# print(is_leapyr(2024))

smart_sub=lambda n1, n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(10,5))