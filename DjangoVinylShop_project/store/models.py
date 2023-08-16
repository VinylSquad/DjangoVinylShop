from django.db import models

from django.urls import reverse
# for dynamic linking


class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)

    class Meta:

        verbose_name_plural = 'categories'

        ordering = ('name',)

    def __str__(self):

        return self.name
    
    
    
    def get_absolute_url(self):

        return reverse('list-category', args=[self.slug])


class Product(models.Model):

    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE, null=True)

    artist = models.CharField(
        max_length=250, null=True, blank=True, db_index=True)

    title = models.CharField(max_length=250)

    label = models.CharField(max_length=250, default='un-labeled')

    release_year = models.PositiveSmallIntegerField(null=True)

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=5, decimal_places=2)

    slug = models.SlugField(max_length=255)

    image = models.ImageField(upload_to='images/')

    class Meta:

        verbose_name_plural = 'products'

        ordering = ('title',)

    def __str__(self):

        return f"{self.artist} - {self.title}"



    # function for dynamic links to products

    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])
