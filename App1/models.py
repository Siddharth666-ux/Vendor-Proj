from django.db import models

class register(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name