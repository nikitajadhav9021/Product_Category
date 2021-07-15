from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=False, max_length=200)
    slug = models.SlugField(null=False)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.SET_NULL)

    class Meta:  
        db_table = "dj_categories"
        # Add verbose name
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        unique_together = ('slug', 'parent',)

class Product(models.Model):
    #token = models.CharField( max_length=20, unique=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    name = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    specification = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    