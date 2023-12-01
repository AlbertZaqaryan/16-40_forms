from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField('Category name', max_length=60)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categ')
    name = models.CharField('Sub category name', max_length=60)
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

class Product(models.Model):

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,related_name='cat_prod')
    name = models.CharField('Product name', max_length=50)
    price = models.PositiveIntegerField('Product price')
    image = models.ImageField('Product image', upload_to='products')
    active = models.BooleanField('Product active')

    def __str__(self):
        return self.name

class Support(models.Model):

    name = models.CharField('Support name', max_length=60)
    email = models.EmailField('Support email')
    message = models.TextField('Support text')

    def __str__(self):
        return self.email