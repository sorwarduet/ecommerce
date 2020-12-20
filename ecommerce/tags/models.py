from django.db import models
from ecommerce.products.utils import generate_unique_slug
from django.template.defaultfilters import slugify
from ecommerce.products.models import Product

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(editable=False, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)


    def __str__(self):
        return  self.title

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Tag, self.title)
        else:  # create
            self.slug = generate_unique_slug(Tag, self.title)
        super(Tag, self).save(*args, **kwargs)



