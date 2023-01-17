from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='News')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Category', db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def get_count(self):
        return len(News.objects.filter(category_id=self.pk))
