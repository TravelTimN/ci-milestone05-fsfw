from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    """
    Ensure user/profile always remain associated and
    deleted using the CASCADE model if profile is deleted.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="profile_imgs/default.png",
        upload_to="profile_imgs",
        blank=True,
        null=True)
    total_donated = models.IntegerField(
        default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        """
        - installed 'django-cleanup' to auto-remove old image.
        - installed 'pillow' to resize larger images.
        """
        img = Image.open(self.image.path)
        if img.height > 200 or img.width > 200:
            new_img_size = (200, 200)
            img.thumbnail(new_img_size)
            img.save(self.image.path)


def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
