from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)


    def __str__(self):
        return f"{self.name} - {self.email}"

# Create your models here.
