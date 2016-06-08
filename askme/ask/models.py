# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, UserManager
from datetime import datetime
from django.db.models import Count

class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name = u"Тэг")

    class Meta:
        verbose_name = u"Тэг"
        verbose_name_plural = u"Теги"

    def __unicode__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name = u'User', related_name = 'users_profile')
    avatar_url = models.CharField(max_length = 255, verbose_name = u'URL аватарки?', null = True)
    nickname = models.CharField(max_length = 255, verbose_name = u'Ник', null = True, unique = True)
    avatar = models.ImageField(upload_to='images',null = True)    

class QuestionManager(models.Manager):
    def hot(self):
        return self.order_by("published_date")
    
    def best(self):
        return self.annotate(num = Count('Liked_users') - Count('DisLiked_users')).order_by('-num')

    def by_tag(self, tag):
        return self.filter(question_tags__title__contains=tag)

    def num_answ(self):
        return self.filter(answer__question__id==id).count()

class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name = u"Название")
    text  = models.TextField(verbose_name = u"Текст")
    question_tags =  models.ManyToManyField(Tag, verbose_name=u'Тэги')
    authors = models.ForeignKey(User, verbose_name=u'Авторы', related_name = 'users_question', null = True)
    Liked_users = models.ManyToManyField(User, related_name = 'Liked_questions')
    DisLiked_users = models.ManyToManyField(User, related_name = 'DisLiked_questions')
    published_date = models.DateTimeField(default=datetime.now, blank=True)

    objects = QuestionManager()
    
    def get_like(self):
        tmp = self.Liked_users.count() - self.DisLiked_users.count()
        return tmp
 
    class Meta:
        verbose_name = u"Вопрос"
        verbose_name_plural = u"Вопросы"

    def __unicode__(self):
        return self.title

#class QuestionHated(models.Model):
#    persons = models.ForeignKey(User, related_name = 'Hated_users')
#    quest = models.ForeignKey(Question, related_name = 'quest')
#
#class QuestionLiked(models.Model):
#    persons = models.ForeignKey(User, related_name = 'Liked_users')
#    quest = models.ForeignKey(Question, related_name = 'quest')

class AnswerManager(models.Manager):
    def answ(self, q_id):
         return self.filter(question__id=q_id)

    def num_answ(self):
        return self.filter(question__id=self.question__id)   

class Answer(models.Model):
    text  = models.TextField(verbose_name = u"Текст", default = 'some text')
    authors = models.ForeignKey(User, verbose_name=u'Авторы', related_name = 'users_answers', null = True)
    Liked_users = models.ManyToManyField(User, related_name = 'Liked_answers')
    DisLiked_users = models.ManyToManyField(User, related_name = 'DisLiked_answers')
    status = models.BooleanField(verbose_name = u"Статус", default = False)
    question = models.ForeignKey(Question, null = True, related_name = 'answ')
    class Meta:
        verbose_name = u"Ответ"
        verbose_name_plural = u"Ответы"

    def get_like(self):
        tmp = self.Liked_users.count() - self.DisLiked_users.count()
        return tmp

    objects = AnswerManager()

    def __unicode__(self):
        return self.text

