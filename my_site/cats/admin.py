from django.contrib import admin

from .models import Pet, Breed

admin.site.register(
    (Pet, Breed)
)








# Register your models here.