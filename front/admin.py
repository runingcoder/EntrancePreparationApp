from django.contrib import admin
from .models import *
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    search_fields = ['text']
    list_filter = ['quiz']    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(MockTest)
admin.site.register(Result)
