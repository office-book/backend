from django.db import models

from company.models import Company

ASSET_STATUS = (
    ('OK', 'OK'),
    ('DECOM', 'DECOM'),
    ('ON REPAIR', 'ON REPAIR')
)


class Asset(models.Model):
    asset_name = models.CharField(max_length=30)
    asset_description = models.TextField()
    asset_serial_number = models.CharField(max_length=50)
    asset_part_number = models.CharField(max_length=50)
    asset_reg_date = models.DateField()
    asset_added = models.DateTimeField(auto_now_add=True)
    asset_last_inspection = models.DateField()
    asset_status = models.CharField(max_length=10, choices=ASSET_STATUS)
    asset_owner = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.asset_name
