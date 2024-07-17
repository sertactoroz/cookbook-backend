from django.db import models
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    def __str__(self):
        return self.title
