import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from cats.models import Pet


class Registration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField()
    cage = models.CharField(max_length=10)
    reg_num = models.CharField(max_length=256, auto_created=True, null=True, blank=True)

    def __str__(self):
        return self.reg_num if self.reg_num else self.date.strftime("%d-%m-%Y")


class Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    note = models.CharField(max_length=256)

    def __str__(self):
        return "{} {}".format(self.lastname, self.firstname)





