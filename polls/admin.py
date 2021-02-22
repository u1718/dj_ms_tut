from django.contrib import admin

# Register your models here.
from .models import Question, Choice

from django.contrib import admin

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
