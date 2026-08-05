#Write a program to implement a Configurable Payment Processing System Using Strategy Pattern.
# Strategy Pattern - Payment Processing System


# Payment Strategies
class CreditCard:
    def pay(self, amount):
        print("Paid Rs.", amount, "using Credit Card")


class UPI:
    def pay(self, amount):
        print("Paid Rs.", amount, "using UPI")


class Cash:
    def pay(self, amount):
        print("Paid Rs.", amount, "using Cash")


# Context Class
class Payment:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def make_payment(self, amount):
        self.payment_method.pay(amount)


# Main Program

print("Choose Payment Method")
print("1. Credit Card")
print("2. UPI")
print("3. Cash")

choice = int(input("Enter your choice: "))
amount = float(input("Enter Amount: "))

if choice == 1:
    method = CreditCard()
elif choice == 2:
    method = UPI()
elif choice == 3:
    method = Cash()
else:
    print("Invalid Choice")
    exit()

payment = Payment(method)
payment.make_payment(amount)
