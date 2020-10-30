from django.contrib import admin
from FirstPage.models import Contact

# Register your models here.
admin.site.register(Contact)
admin.site.site_header = "Pindi Official Admin"
admin.site.site_title = "Pindi Official Admin Portal"
admin.site.index_title = "Welcome to Pindi Official Portal"