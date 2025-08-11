from django.db import models
from django.urls import reverse
class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('reserved', 'Reserved'),
    ]
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    isbn = models.CharField(max_length=20, blank=True)
    published_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return f"{self.title} — {self.author}"
    def get_absolute_url(self):
        return reverse('catalog:book-detail', args=[str(self.id)])
