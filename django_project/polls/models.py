from django.db import models

# Create your models here.


class Question(models.Model):   # 테이블 선언

    # name : question_text / type : varchar(200)
    question_text = models.CharField(max_length=200)
    # question_text = models.ForeignKey('Choice', on_delete=models.CASCADE)

    # name : pub_date / type : datetime
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):

    # name : question_id / type : integer / FK 연결
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # name : choice_text / type : varchar(200)
    choice_text = models.CharField(max_length=200)

    # name : votes / type : integer / 기본값 = 0 지정
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
