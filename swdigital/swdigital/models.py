from django.db import models

class AccountInfo(models.Field):
    account= models.CharField(max_length=30)
    accountnumber = models.CharField(max_length=30)
    status_types = (
        (1, "无风险"),
        (2, "待检查"),
        (3, "有风险"),
    )
    checkstatus = models.IntegerField(choices=status_types,default=2)

class PayIn(models.Field):
    account = models.ForeignKey(AccountInfo)
    price = models.FloatField()
    datetime = models.DateField()

class PayOut(models.Field):
    account = models.ForeignKey(AccountInfo)
    price = models.FloatField()
    datetime = models.DateField()