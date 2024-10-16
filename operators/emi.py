# calculate emi

p=200000
r=9
t=20
rate=r/(12*100)
tenure=t*12
emi=(p*rate*(1+rate)**tenure/((1+rate)**tenure-1))
print("EMI=",emi)
interest_payable=(emi*tenure)-p
print("Interest payable=",interest_payable)
total_payment=p+interest_payable
print("Total payment=",total_payment)
