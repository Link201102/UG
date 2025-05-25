from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user","product","rating")
    list_filter = ("user", "product")
    search_fields = ("user", "product")