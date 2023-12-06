from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)

# 새로운 테이블 생성 시, admin에 반드시 등록할 것
# 그 후, 아래의 명령어를 작업할 것
# python manage.py makemigrations
# python manage.py migrate