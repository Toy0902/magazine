from django.db import models
class Email(models.Model):
    email = models.CharField(max_length=222)
    text = models.TextField()
    subject = models.CharField(max_length=777)
    ismi = models.CharField(max_length=300)
    phone = models.IntegerField()

    def __str__(self):
        return self.ismi
# Create your models here.
