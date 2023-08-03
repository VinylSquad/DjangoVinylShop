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

    artist  = models.CharField(max_length=250)

    title = models.CharField(max_length=250)

    label = models.CharField(max_length=250, default='un-labeled')
    
    release_date = models.DateField('Release Date', year_field='release_year')

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=5, decimal_places=2)

    slug = models.SlugField(max_length=255)

    image = models.ImageField(upload_to='images/')

    
    # Dodajemy metodę, aby łatwiej ustawiać rok wydania
    def set_release_year(self, year):
        
        self.release_date = year
    
    
    def save(self, *args, **kwargs):
        if self.release_date:
            self.release_date = self.release_date.replace(month=1, day=1)
        super(Product, self).save(*args, **kwargs)
    
    

    class Meta:

        verbose_name_plural = 'products'

        ordering = ('title',)

    def __str__(self):

        return self.title




    # function for dynamic links to products 
    def get_absolute_url(self):
        
        return reverse('product-info', args=[self.slug])