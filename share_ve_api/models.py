from django.db import models

class User(models.Model):

    MEMBERSHIP_HOST = 'H'
    MEMBERSHIP_GUEST = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_HOST, 'Host'),
        (MEMBERSHIP_GUEST, 'Guest')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_GUEST)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

