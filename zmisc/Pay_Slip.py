b=100000#int(input("Enter basic Salary: "))
DA=b/2
TA=b*3/10
HR=b*24/100
Other_A=b/10
PF=b*12/100
Tax=b/20
Net=round(100*(DA+TA+HR+Other_A-PF-Tax))/100
if Net>500000:
	pos="Manager"
elif 500000>Net>400000:
	pos="Clerk"
else:
	pos="Peon"
print( "				Pay Slip\n")
print( "				Name:	XYZABCD")
print(f"				Post: {pos}")
print(f"Basic Salary: {b}")
print(f"					DA: {DA}")
print(f"					HR: {HR}")
print(f"			Others: {Other_A}")
print(f"					PF: {PF}")
print(f"			 Taxes: {Tax}")
print(f"	Net Salary: {Net}")
