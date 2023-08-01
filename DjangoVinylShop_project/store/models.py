from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)

    class Meta:

        verbose_name_plural = 'categories'

        ordering = ('name',)

    def __str__(self):

        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=250)

    label = models.CharField(max_length=250, default='un-labeled')

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=5, decimal_places=2)

    slug = models.SlugField(max_length=255)

    image = models.ImageField(upload_to='images/')


    class Meta:

        verbose_name_plural = 'products'

        ordering = ('title',)

    def __str__(self):

        return self.title