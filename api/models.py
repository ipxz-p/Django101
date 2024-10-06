from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator

class User(models.Model):
    first_name = models.CharField(max_length=50, default='Firstname')
    last_name = models.CharField(max_length=50, default='Lastname')
    email = models.EmailField(max_length=254, unique=True, validators=[EmailValidator()], default='example@example.com')
    password = models.CharField(max_length=128, default='password')

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"