from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

# Create your models here.

CHOICES = [('text_response', 'TextResponse'), ('one_option_response', 'OneOptionResponse'), ('multiple_answer_options', 'MultipleAnswerOptions')]


class Poll(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    start_date = models.DateField(blank=False, null=False, verbose_name='Дата старта')
    finish_date = models.DateField(blank=False, null=False, verbose_name='Дата финиша')

    class Meta:
        db_table = 'Polls'
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self):
        return self.title



class Question(models.Model):
    poll = models.ForeignKey('api_v1.Poll', blank=False, null=False, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=1000, blank=False, null=False, verbose_name='Текст вопроса')
    type = models.CharField(max_length=100, choices=CHOICES, default='text_response', verbose_name='Тип')

    class Meta:
        db_table = 'Questions'
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey('api_v1.Question', blank=False, null=False, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, blank=False, null=False)

    class Meta:
        db_table = 'Choices'
        verbose_name = "Выбор"
        verbose_name_plural = "Выборы"

    def __str__(self):
        return self.text


class AnswChecker(models.Model):
    user = models.IntegerField(blank=False, null=False, verbose_name='user')
    question = models.ForeignKey('api_v1.Question', blank=False, null=False, verbose_name='Вопрос', related_name='answer_checker', on_delete=models.CASCADE)
    choice = models.ForeignKey('api_v1.Choice', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Выбор', related_name='answer_checker')
    answer = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'AnswCheckers'
        verbose_name = "Мониторинг ответа"
        verbose_name_plural = "Мониторинг ответов"