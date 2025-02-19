from django.contrib import admin
from .models import Book,Blog

# Register the Book model with the Django admin site
admin.site.register(Book)
admin.site.register(Blog)