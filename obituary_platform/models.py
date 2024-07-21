from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Obituary(models.Model): 
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField()
    author = models.CharField(max_length=50)
    submission_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta: 
        verbose_name_plural = 'Obituaries'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            formatted_name = '-'.join(self.name.split()).lower()
            formatted_dob = self.date_of_birth.strftime('%Y-%d-%m')
            self.slug = slugify(f'{formatted_name}-{formatted_dob}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('obituary_detail', args=[self.slug])
