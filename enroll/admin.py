from django.contrib import admin
from .models import SudentModel

# Register your models here.
@admin.register(SudentModel)
class ModelAdmin(admin.ModelAdmin):
  display_list=['id','name','email', 'password'] 
