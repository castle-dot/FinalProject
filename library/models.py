from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class LibraryUser(AbstractUser):
    date_of_membership = models.DateField(default=timezone.now)
    is_active_member = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    copies_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.author}"
