from django.db import models

from company.models import Company

STAFF_TYPE = (
    ('PROBATION', 'PROBATION'),
    ('FULL_STAFF', 'FULL_STAFF'),
    ('CONTRACT', 'CONTRACT'),
)

STAFF_STATUS = (
    ('ACTIVE', 'ACTIVE'),
    ('SACKED', 'SACKED'),
    ('RESIGNED', 'RESIGNED'),
    ('RETIRED', 'RETIRED'),
)


class Staff(models.Model):
    staff_first_name = models.CharField(max_length=20)
    staff_middle_name = models.CharField(max_length=20)
    staff_last_name = models.CharField(max_length=20)
    staff_DOB = models.DateField()
    staff_personal_email = models.EmailField()
    staff_official_email = models.EmailField(blank=True, null=True)
    staff_phone = models.CharField(max_length=50)
    staff_employment_date = models.DateField()
    staff_role = models.CharField(max_length=20)
    staff_employment_status = models.CharField(choices=STAFF_STATUS, max_length=15)
    staff_type = models.CharField(choices=STAFF_TYPE, max_length=15)
    staff_salary = models.FloatField()
    staff_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    staff_added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_first_name + self.staff_last_name
