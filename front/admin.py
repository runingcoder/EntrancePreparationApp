from django.contrib import admin
from .models import *
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer
    
    
@admin.action(description='Change the quiz id to 15')
def change_quizid(modeladmin, request, queryset):
    queryset.update(quiz_id=15)
    
def copy_to_physicsIOM(modeladmin, request, queryset):
    for obj in queryset:
        ringo = Question.objects.create(text=obj.text, quiz_id=27)
        for ans in obj.answer_set.all():
            Answer.objects.create(text=ans.text, correct=ans.correct, question=ringo)
        ringo.save()
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    search_fields = ['text']
    list_filter = ['quiz'] 
    actions = [change_quizid, copy_to_physicsIOM] 
    
 
      
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(MockTest)
admin.site.register(Result)
