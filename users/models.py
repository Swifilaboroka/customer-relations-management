from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# organization
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')

    def __str__(self):
        return self.user.email


def post_user_create_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user_id=instance.id)

post_save.connect(post_user_create_signal, sender=CustomUser)
