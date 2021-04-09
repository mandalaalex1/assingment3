# Enter Full Names
print("Enter First and Last Name:")
fname = input("First Name ")
lname = input("last Name ")
fullnames = (fname + " " + lname)

# Enter phone, email
print("Enter Customer's Phone Number: ")
phone = input("phone")
print("Enter Customer's email address: ")
email = input("email")

# print("Phone: " +phone)
# print("Email: " +email)

# price of a used car
price = 10000
has_good_credit = float(input("what is your credit score?"));

if has_good_credit > 700:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

# print ("{0:.2f}".format(down_payment))
s = "\033[1m"
e = "\033[0;0m"

print("")
print(s + "Full Names: " + e + fullnames)
print(s + "Phone: " + e + phone)
print(s + "Email: " + e + email)
print(s + "Down Payment:" + e, ("{0:.2f}".format(down_payment)))