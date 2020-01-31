import uuid
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models
from django.urls import reverse



class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Pet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=256,)
    age = models.IntegerField(validators=[validators.MaxValueValidator(100)])
    doc = models.ForeignKey('cat.Registration', on_delete=models.CASCADE,related_name="pet_registration")
    photo = models.ImageField(upload_to='pets_photo', blank=True)
    breed = models.ForeignKey('cats.Breed', on_delete=models.CASCADE)
    owner = models.ForeignKey("cat.Owner", on_delete=models.CASCADE, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        self.doc.reg_num = self.breed.name[0] + self.doc.date.strftime(
            "%d%m%Y")
        self.doc.save()
        super().save()

    def make_word_end(self):
        word = "лет"
        n = self.age
        if n > 99:
            n = n % 100
        if n in range(5, 21):
            word = "лет"
        elif n % 10 == 1:
            word = "год"
        elif n % 10 in range(2, 5):
            word = "года"
        return "{} {}".format(self.age, word)

    def __str__(self):
        return "{} ({}, {})".format(self.name, self.breed,
                                    self.make_word_end())

    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'pk': self.pk})




