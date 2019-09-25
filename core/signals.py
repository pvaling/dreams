from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from core.models import Profile


@receiver(post_save, sender=User)
def new_user_signal(sender, instance: User, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            profile = instance.profile
            profile.save()
        except Exception:
            Profile.objects.create(user=instance)



