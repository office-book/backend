from django.db import models


class UserType(models.Model):
    user_type = models.CharField(max_length=25)

    def __str__(self):
        return self.user_type
