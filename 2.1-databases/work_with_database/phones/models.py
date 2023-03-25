from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название модели", null=False, max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.URLField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True,db_index=True,verbose_name='URL')

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    pass
