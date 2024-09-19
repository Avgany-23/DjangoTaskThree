from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator


class Phone(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.BigIntegerField(null=True)
    image = models.ImageField(
        default='default_phone.png',
        upload_to='phones',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])
    release_data = models.DateField(null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Модель: {self.name}, {self.image=}'

    class Meta:
        unique_together = [['name', 'price'], ]
