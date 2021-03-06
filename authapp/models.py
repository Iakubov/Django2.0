from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='Age', default=18)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        default=now() + timedelta(hours=48)
    )

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'W')
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False,
                                db_index=True, on_delete=models.CASCADE)
    tagLine = models.CharField(verbose_name='tags', max_length=128, blank=True)
    aboutMe = models.CharField(verbose_name='about', max_length=512, blank=True)
    gender = models.CharField(verbose_name='sex', max_length=1,
                              choices=GENDER_CHOICES, blank=True)
    profile_link = models.CharField(verbose_name='vk_link', max_length=128, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
