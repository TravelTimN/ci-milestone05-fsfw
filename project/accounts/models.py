from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    """
    Ensure user/profile always remain associated and
    deleted using the CASCADE model if profile is deleted.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="profile_imgs/default.png",
        upload_to="profile_imgs")

    def __str__(self):
        return f"{self.user.username}'s Profile"


def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
