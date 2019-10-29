from django.db import models
from datetime import date

# Create your models here.

# class for add destination place
class Destinations(models.Model):
    
    name = models.CharField(max_length=100)
    img  = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    date = models.DateTimeField()
    published = models.BooleanField(default=True)

#class for add banner image and text of banner slider 
class Banner(models.Model):
    banner_img = models.ImageField(upload_to='pics')
    banner_text = models.TextField()

#class for change testimonial description 
class Testimonials(models.Model):
    cname = models.TextField()
    test_img = models.ImageField(upload_to='pics')
    test_desc = models.TextField()

#class for add new news 
class News_Details(models.Model):
    date = models.DateTimeField()
    heading = models.CharField(max_length=100)
    news_img = models.ImageField(upload_to='pics')
    categories = models.CharField(max_length=100)
    news_desc = models.CharField(max_length=300)

#discount offers 
class offersDetails(models.Model):
    offer_img = models.ImageField(upload_to='pics')
    offer_type = models.CharField(max_length=50)
    offer_desc = models.CharField(max_length=100)

#about page 
class aboutUs(models.Model):
    banner_img = models.ImageField(upload_to='pics')

    about_heading = models.CharField(max_length=100)

    about_desc = models.CharField(max_length=100)

   # view 
    about_icon = models.ImageField(upload_to='pics')

    # why chose us

    why_banner = models.ImageField(upload_to='pics')
    card_img = models.ImageField(upload_to='pics')
    card_title = models.CharField(max_length=100)
    card_desc = models.CharField(max_length=100)

    # Team Section 

    team_img = models.ImageField(upload_to='pics')
    team_name = models.CharField(max_length=20)
    team_desc = models.CharField(max_length=100)

   
    
