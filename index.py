employeeName=input("Enter Employee name: ")
shifts=int(input("Enter number of shifts: "))
transactionsNumber=int(input("Enter number of transactions: "))
transactionValue=int(input("Enter transaction dollar value: "))
print("\n")

productivityScore=(transactionValue/transactionsNumber)/shifts
bonus=0
if productivityScore<=30:
    bonus=50
elif 31<=productivityScore<=69:
    bonus=75
elif 70<=productivityScore<=199:
    bonus=100
else:
    bonus=200
    
print(f'Employee name: {employeeName}')
print(f'Employee balance: ${bonus}')
