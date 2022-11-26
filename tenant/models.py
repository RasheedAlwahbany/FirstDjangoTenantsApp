from django.db import models

# Create your models here.
class Tenant(models.Model):
    name=models.CharField(max_length=200)
    subdomain=models.CharField(max_length=200)
    
class TenantAwareMode(models.Model):
    tenant=models.ForeignKey(Tenant,on_delete=models.CASCADE)
    
class Member(TenantAwareMode):
    name=models.CharField(max_length=200)