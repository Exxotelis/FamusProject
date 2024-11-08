from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    genre = models.CharField(max_length=50)
    tags = models.CharField(max_length=255)
    game_id = models.CharField(max_length=50)
    reviews_count = models.IntegerField(default=0)
    reviews_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
