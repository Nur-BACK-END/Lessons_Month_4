from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'Category: {self.title}'
    
class Tag(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Teg: {self.title}"


class Post(models.Model):
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400,blank=True)
    rate = models.IntegerField(default=0)
    content = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="posts",null=True,blank=True)
    tag = models.ManyToManyField('Tag', related_name="posts", blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.description}"
    
