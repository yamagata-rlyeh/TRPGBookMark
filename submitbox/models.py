from django.conf import settings
from django.db import models
from django.utils import timezone

class AppUser(models.Model):
    
    user_id = models.CharField(max_length=50)
    user_pass  = models.CharField(max_length=50)


    def __str__(self):
        return self.user_id

class CharacterSheet(models.Model):
    user_name = models.ForeignKey('AppUser',on_delete=models.CASCADE,null=True,blank=True)
    character_name = models.CharField(max_length=50)
    system_name = models.CharField(max_length=30)
    user_comment = models.TextField(blank=True)
    page_url = models.URLField(blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.character_name
