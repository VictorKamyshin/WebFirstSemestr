from django.contrib import admin
from ask.models import Question, Tag, Answer, Profile

class QuestionAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class AnswerAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
