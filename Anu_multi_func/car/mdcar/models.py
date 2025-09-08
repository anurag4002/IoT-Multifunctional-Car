from django.db import models

# Create your models here.

class Parts(models.Model):
    sn = models.AutoField(primary_key=True)
    img = models.ImageField( upload_to='parts/', height_field=None, width_field=None, max_length=None, default=True)
    title = models.CharField( max_length=100, default=True)
    content = models.CharField( max_length=500, default=True)
    link = models.CharField( max_length=200, default=True)
    time = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-increment primary key
    name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=150, default="")
    contact = models.CharField(max_length=15, default="")  # <-- not primary key anymore
    topic = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name
