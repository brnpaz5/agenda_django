from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    describe = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField(verbose_name='Events')
    creation_date = models.DateTimeField(auto_now=True)
    user_event = models.ForeignKey(User, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'event'
    
    def __str__(self):
        return self.title
    
    def get_date_event(self):
        return self.event_date.strftime('%d/%m/%Y %H:%M')