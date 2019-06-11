from django.contrib import admin
from .models import Dog, Feeding

# Register your models here.
from .models import Dog
admin.site.register(Dog)
admin.site.register(Feeding)
