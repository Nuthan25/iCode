from django.contrib import admin

# Register your models here.
from .models import contact
from .models import registration

admin.site.register(contact)
admin.site.register(registration)