

from django.db import models

class BalanceSheet(models.Model):
    company_name = models.CharField(max_length=255)
    total_assets = models.FloatField()
    total_liabilities = models.FloatField()
    equity = models.FloatField()
    date = models.DateField()

class PLStatement(models.Model):
    company_name = models.CharField(max_length=255)
    revenue = models.FloatField()
    expenses = models.FloatField()
    net_income = models.FloatField()
    date = models.DateField()

class CashFlowStatement(models.Model):
    company_name = models.CharField(max_length=255)
    operating_activities = models.FloatField()
    investing_activities = models.FloatField()
    financing_activities = models.FloatField()
    net_cash_flow = models.FloatField()
    date = models.DateField()
