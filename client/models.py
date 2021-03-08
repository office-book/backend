from django.db import models

from company.models import Company


class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_address = models.TextField()
    client_email = models.EmailField()
    client_email_cc = models.EmailField()
    client_phone = models.CharField(max_length=20)
    client_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    client_added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name
