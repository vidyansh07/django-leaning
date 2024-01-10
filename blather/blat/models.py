from django.db import models

# Create your models here.
class Blat(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    via =models.URLField(blank=True)
    
    def total_likes(self):
        return self.like_set.count()

class Like(models.Model):
    blat = models.ForeignKey(Blat)
