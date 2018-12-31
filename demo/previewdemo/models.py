from django.db import models
from django.shortcuts import reverse

class GenericModel(models.Model):
    data = models.TextField(default='')

    def get_absolute_url(self):
        return reverse('view', args=[self.pk])
