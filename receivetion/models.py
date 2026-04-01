from django.db import models

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, default="Attendee")
    reg_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Idea(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description