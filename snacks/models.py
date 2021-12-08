from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField, TextField
from django.urls import reverse

# Create your models here.

class Snack(models.Model):
    name=CharField(max_length=64)
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description=TextField()

    def get_absolute_url(self):
        return reverse('snack_detail',args=[self.id])

    def __str__(self):
        return self.name 