from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.SubjectMetaData)
admin.site.register(models.StudentMetaData)