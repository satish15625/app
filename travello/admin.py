from django.contrib import admin
from .models import Destinations
from .models import Banner
from .models import Testimonials
from .models import News_Details
from .models import offersDetails
from .models import aboutUs
# Register your models here.
admin.site.register(Destinations)
admin.site.register(Banner)
admin.site.register(Testimonials)
admin.site.register(News_Details)
admin.site.register(offersDetails)
admin.site.register(aboutUs)