from django.db import models


# Create your models here.
class transactionDetail(models.Model):
	name = models.CharField('Transactions Name', max_length = 100)
	email = models.EmailField('Transaction Email',max_length = 100)
	debitted_amt = models.IntegerField()
	credited_amt = models.IntegerField()
	account_bal = models.IntegerField()
	def __str__(self):
		return self.name

class customerDetail(models.Model):
	name = models.CharField('Customer Name', max_length = 100)
	email = models.EmailField('Customer Email', max_length = 100)
	available_bal = models.IntegerField()

	def __str__(self):
		return self.name