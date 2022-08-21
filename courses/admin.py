from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import  courses ,lesson,comment_lesson,gatogery_course # Author, Genre, Book, BookInstance

class courseeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
# # # Register your models here.

admin.site.register(courses,courseeModelAdmin)
admin.site.register(lesson)
admin.site.register(comment_lesson)
admin.site.register(gatogery_course)