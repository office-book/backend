from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from company.models import Company


class UserType(models.Model):
    user_type = models.CharField(max_length=20)

    def __str__(self):
        return self.user_type


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True,)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)

