from django.contrib import admin

from poll.models import Question, Choice

admin.site.register(Choice)
admin.site.register(Question)
