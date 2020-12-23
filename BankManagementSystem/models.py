from django.db import models

# Create your models here.

class Banks(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name 


class CreateAccount(models.Model):

    TYPE = (
        ('Savings Account', 'Savings Account'),
        ('Current Account', 'Current Account'),
        )

    bank_name = models.ForeignKey(Banks, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    contact = models.BigIntegerField()
    date_of_birth = models.DateField()
    branch = models.CharField(max_length=20)
    account_number = models.BigIntegerField()
    account_type = models.CharField(max_length=20, choices=TYPE)
    bank_code = models.CharField(max_length=20)
    insert_amount = models.IntegerField()
    
    def __str__(self):
        self.customer_name
# class BankDetails(models.Model):
#     bank_name = models.ForeignKey(Banks, on_delete=models.CASCADE)
#     branch = models.CharField(max_length=20)
#     account_holder = models.CharField(max_length=20)
#     account_number = models.IntegerField(max_length=20)
#     account_type = models.CharField(max_length=20)
#     bank_code = models.CharField(max_length=20)

#     def __str__(self):
#         return self.bank_name
    
class Transactions(models.Model):
    date = models.DateTimeField()
    cash_deposit = models.CharField(max_length=20)
    reference = models.CharField(max_length=20)
    withdrawal = models.IntegerField()
    deposit = models.CharField(max_length=20)
    balance = models.CharField(max_length=20)

    def __str__(self):
        return self.date