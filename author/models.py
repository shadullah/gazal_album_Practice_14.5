from django.db import models

# Create your models here.
class Author(models.Model):
    f_nm = models.CharField(max_length=15)
    l_nm = models.CharField(max_length=15)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    instru_type = models.CharField(max_length=10)

    def __str__(self):
        return self.f_nm