from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from .utils import generate_unique_slug
from django.shortcuts import reverse

# Create your models here.


class ProductQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)

    def search(self,query):
        lookup = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        return self.filter(lookup).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=30.15)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Product, self.title)
        else:  # create
            self.slug = generate_unique_slug(Product, self.title)
        super(Product, self).save(*args, **kwargs)


    def get_absolute_url(self, *args, **kwargs):
        return reverse('products:detail', kwargs={'slug': self.slug})

