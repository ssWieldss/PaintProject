from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Man(models.Model):
    """Represents user account in database"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_man_profile(sender, instance, created, **kwargs):
    """Controls post method for user registration"""
    if created:
        Man.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_man_profile(sender, instance, **kwargs):
    """Saving user profile instance"""
    instance.man.save()
