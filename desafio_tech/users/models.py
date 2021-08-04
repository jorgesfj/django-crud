from django.db import models

class User(models.Model):
    email = models.EmailField()
    cpf = models.CharField(max_length=100)

    def __str__(self):
        return self.email
