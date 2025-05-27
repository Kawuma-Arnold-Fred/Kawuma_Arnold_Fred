class Payment:
    def pay(self):
        print('Scanning items')
        
class CreditCard(Payment):
    def pay(self):
        print('Paying with credit card')
        
class DigitalPayment(Payment):
    def pay(self):
        print('Paying with mobile app')
        
class PaymentMethod(CreditCard, DigitalPayment):
    pass

Fred = DigitalPayment()
Fred.pay()
print(f'Method Resolution Order: {PaymentMethod.__mro__}')