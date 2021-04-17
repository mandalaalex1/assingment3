#Enter the price of the House you wish to Buy
print("Enter the house price")
price = float(input())

#Enter the credit score
print("Enter the credit score")
CreditScore = input()

#Enter the first name
print("Enter the first name")
first_name = input()

#Enter the last name
print("Enter the last name")
last_name = input()
fullnames = first_name + " " + last_name

#Enter the email
print("Enter the email address")
email = input()#Enter the phone number
print("Enter the phone number")
phone = input()

#Enter the mailing
print("Enter the mailing address")
physicaladdress = input()

#Enter the mailing
print("Enter the City")
city = input()

#Enter the mailing
print("Enter the State")
state = input()

#Enter the mailing
print("Enter the zip code")
zipcode = input()

#Qualify for loans with the best interest rate
if int(CreditScore) >=780 and int(CreditScore)<=850:
 print ("Excent Credit")
 print("Zero Down Payment")
 downPayment = 0.0 * price
 credit_status = ("Zero Down Payment")

#Usually qualify for loans with the best interest rates
if int(CreditScore) >= 740 and int(CreditScore)<=779:
 print("Very Good")
 downPayment = 0.2 * price
 credit_status = ("Very Good")

#May face slightly higher loan Interest rates
if int(CreditScore) >= 720 and int(CreditScore)<=739:
 print("Above Average")
 downPayment = 0.3 * price
 credit_status = ("Above Average")

#May qualify for most loans of higher interest rates
if int(CreditScore) >= 680 and int(CreditScore)<=719:
  print("Average")
  downPayment = 0.6 * price
  credit_status = ("Average")

#May qualify for most loans at significant higher Interest rates
if int(CreditScore) >= 620 and int(CreditScore)<=679:
 print("Below Average")
 downPayment = 0.18 * price
 credit_status = ("Below Average")
elif int(CreditScore) >= 580 and int(CreditScore)<=619:
 print("Poor Credit Score")
 downPayment = 0.20 * price
 credit_status = ("Poor Credit Score")


s = "\033[1m"
e = "\033[0;0m"

print("")
print("="*60)
print(s + "Full Name:" + e + fullnames)
print(s + "Physical Address:" + e + physicaladdress)
print(s + "City:" + e + city, s + "State:" + e + state, s + "Zipcode:" + e + zipcode)
print("")
print(s + "New House Price:" + e ,("{0:.2f}".format(price)))
print(s + "Down Payment:"+ e ,("{0:.2f}".format(downPayment)))
print(s + "Credit Score:" + e + str(CreditScore))
print(s + "Credit Score:" + e + credit_status)
print("")
print("="*60)
print(s + "CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME - " + e + fullnames)
print("="*60)