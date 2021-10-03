from django.core.files.base import ContentFile
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from sorl.thumbnail import get_thumbnail, delete

import uuid


def image_directory_path(instance, filename):
    return f'images/{str(uuid.uuid4())}.{filename.split(".")[-1]}'


class Image(models.Model):
    image = models.ImageField(upload_to=image_directory_path)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        tmp_img_name = self.image.name
        if self.image.width > 500 or self.image.height > 500:
            new_width = 500
            new_height = 500

            resized = get_thumbnail(self.image, f'{new_width}x{new_height}')
            name = resized.name.split('/')[-1]
            self.image.save(name, ContentFile(resized.read()), True)

            try:
                delete(tmp_img_name)
            except ObjectDoesNotExist as e:
                print(e)