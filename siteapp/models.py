from django.db import models

# Create your models here.

class Review(models.Model):
    username = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.date}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["date"]

