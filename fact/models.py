from django.db import models


class Person(models.Model):
    identification_number = models.CharField(max_length=25, unique=True,
                                             blank=False, null=False)
    first_name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    birth_date = models.DateField(default=datetime.date.today)


class Company(models.Model):
    owner = models.ForeignKey('fact.Person', related_name='companies',
                              unique=True)
    ruc = models.CharField(max_length=250, blank=False, null=False)
    name = models.CharField(max_length=250, blank=False, null=False)
    sri_auth = models.CharField(max_length=250, blank=False, null=False)


class Customer(Person):
    created = models.DateField(default=datetime.date.today)
    updated = models.DateField()


class Invoice(models.Model):
    created = models.DateField(default=datetime.date.today)
    updated = models.DateField()
    number = models.CharField(max_length=50, blank=False, null=False)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    discount = models.DecimalField(max_digits=12, decimal_places=2)
    company = models.ForeignKey('fact.Company', related_name='invoices')
    customer = models.ForeignKey('fact.Customer', related_name='invoices')


class Category(models.Model):
    created = models.DateField(default=datetime.date.today)
    updated = models.DateField()
    name = models.CharField(max_length=250, blank=False, null=False)


class Product(models.Model):
    created = models.DateField(default=datetime.date.today)
    updated = models.DateField()
    name = models.CharField(max_length=250, blank=False, null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey('fact.Category', related_name='products')


class InvoiceDetail(models.Model):
    product = models.ForeignKey('fact.Product', related_name='details')
    invoice = models.ForeignKey('fact.Invoice', related_name='details')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=250, blank=False, null=False)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)


class Transaction(models.Model)
    created
    updated
    description
    type
    amount


class AccountigRegister(models.Model):
    created
    updated
    description
    debit
    assets
    balance
    account
    transaction


class Ledger(models.Model):
    created
    updated
    debit
    assets
    balance
    transaction


class Payment(models.Mode):
    created
    updated
    amount
    description
    customer
    accountigRegister
