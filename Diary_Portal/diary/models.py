from django.db import models
from datetime import datetime
# Create your models here.
class company(models.Model):
    CompanyName = models.CharField(max_length=100)
    POC         = models.CharField(max_length=100)
    CPOC        = models.CharField(max_length=100)
    order       = models.AutoField(primary_key=True)
    TopRemark   = models.TextField()
    placement   = models.BooleanField()
    def __str__(self):
        return self.CompanyName

class remarks(models.Model):
    company = models.ForeignKey(company,on_delete=models.CASCADE,default=0)
    remark = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    CPOC = models.CharField(max_length=100)
    POC = models.CharField(max_length=100)
    def __str__(self):
        return self.company.CompanyName


