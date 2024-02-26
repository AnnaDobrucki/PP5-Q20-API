from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

class DNDEvent(models.Model):
    # partial templates from CI walkthrough of moments 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=255)  
    game_description = models.TextField(blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(default=date.today)
    game_master = models.CharField(max_length=255, blank=True) 
    event_location = models.TextField(blank=True)
    event_start = models.TimeField(default=timezone.now)
    event_end = models.TimeField(default=timezone.now)
    contact = models.EmailField(blank=True)
    image = models.ImageField(upload_to='images/', default='../placeholder', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.game_name}'