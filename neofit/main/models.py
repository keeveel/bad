from django.db import models


# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    lessons_count = models.IntegerField(verbose_name='Количество уроков')
    lessons_duration = models.FloatField(verbose_name='Количество минут для одного урока')
    lessons_logo = models.ImageField(verbose_name='Логотип урока')

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Student(models.Model):
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.date_of_birth}: {self.lesson}"

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
