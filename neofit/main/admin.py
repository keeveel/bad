from django.contrib import admin
from .models import (
    Lesson,
    Student
)


admin.site.register(Lesson)
admin.site.register(Student)
