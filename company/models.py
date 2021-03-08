from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=50)
    company_address = models.TextField()
    company_email = models.EmailField()
    company_email_cc = models.EmailField(blank=True, null=True)
    company_phone = models.CharField(max_length=30)
    company_RC = models.CharField(max_length=20)
    company_registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
