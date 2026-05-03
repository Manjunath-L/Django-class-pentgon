from django.db import models
from django.utils.text import slugify

# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    teacher = models.CharField(max_length=100)
    no_students = models.IntegerField()
    batch = models.CharField(max_length=10)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        base_slug = slugify(self.name) or "class"
        slug = base_slug
        counter = 1
        queryset = Class.objects.filter(slug=slug)
        if self.pk:
            queryset = queryset.exclude(pk=self.pk)

        while queryset.exists():
            slug = f"{base_slug}-{counter}"
            queryset = Class.objects.filter(slug=slug)
            if self.pk:
                queryset = queryset.exclude(pk=self.pk)
            counter += 1
        return slug

    def __str__(self):
        return self.name
