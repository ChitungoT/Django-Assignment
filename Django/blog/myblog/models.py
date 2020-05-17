from django.db import models

#categories
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

#Articles
class Articles(models.Model):
    cateregory = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.TextField()
    
