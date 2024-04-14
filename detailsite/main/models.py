from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_role = models.CharField('Роль пользователя', max_length=200, default='User')


class Detail(models.Model):
    detail_image = models.ImageField('Изображение',upload_to='detail_img/', null=True, blank=True)
    detail_name = models.CharField('Название', max_length=100)
    detail_size = models.CharField('Размер', max_length=100)
    detail_color = models.CharField('Цвет', max_length=100)
    detail_material = models.CharField('Материал', max_length=100)
    detail_description = models.TextField('Описание', max_length=500, default='')

    def __str__(self):
        return f'| {self.detail_name} |'

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'
