from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='News')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']
    

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Category', db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
