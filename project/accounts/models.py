from django.db import models
from django.core.files.storage import default_storage as storage
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image, ImageOps


def upload_to(instance, filename):
    return "profiles/%s/%s" % (instance.user.username, filename)


class Profile(models.Model):
    """
    Ensure user/profile always remain associated and
    deleted using the CASCADE model if profile is deleted.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="profiles/default.png",
        upload_to=upload_to,
        blank=True,
        null=True)
    total_donated = models.IntegerField(
        default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        """
        - installed 'django-cleanup' to auto-remove old image.
        - installed 'pillow' to resize larger images.
        - resizes all image formats except '.gif' as these cannot be resized
        """
        super(Profile, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image)
            if img.format.lower() != "gif":
                size = 300
                thumb = (size, size)
                method = Image.ANTIALIAS
                center = (0.5, 0.5)
                extension = "png"
                if img.height > size or img.width > size:
                    img.thumbnail((size, size), method)
                    new = ImageOps.fit(img, thumb, method, centering=center)
                    temp = storage.open(self.image.name, "w")
                    new.save(temp, extension)
                    temp.close()
                    super(Profile, self).save(*args, **kwargs)


def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
