from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('数据的日期',       {'fields': ['pub_date']}),
    ]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.index_title = '智能柜子数据管理'  # 登陆标题

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
