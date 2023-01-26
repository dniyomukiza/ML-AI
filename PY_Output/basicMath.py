numHours= input("Enter the number of hours: ")
hourlyRate = input("Enter rate: ")
totalPay = float(numHours) * float(hourlyRate)
overtimeRate = 1.5
overtimePay = totalPay + float(numHours) * overtimeRate
if float(numHours) <= 40 :
        print("Regular pay is: ",totalPay)
else:
        print("Overtime pay is: ",overtimePay)
