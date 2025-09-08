from django.contrib import admin
from mdcar.models import Parts, Contact


# Admin modifyng
admin.site.site_header = 'Multifunctional Car'
admin.site.site_title = 'Multifunctional Car'
admin.site.index_title = 'Welcome to Multifunctional Car Administration'


# Register your models here.
admin.site.register(Parts)
admin.site.register(Contact)

