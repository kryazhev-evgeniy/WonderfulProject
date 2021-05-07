from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import uuid

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    image = models.URLField(verbose_name="Изображение", null=True, blank=True)
    views = models.IntegerField(verbose_name="Просмотры", default=0)
    likes = models.IntegerField(verbose_name="Лайки", default=0)
    male = models.BooleanField(verbose_name="мужской зал (по умолчанию женский)",default=False)

    class Meta:
        managed = True
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.name

class Order(models.Model):
    user_order = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="пользователь")
    service_order = models.ForeignKey(Service,on_delete=models.CASCADE, verbose_name="Услуга")
    date = models.DateField(verbose_name="Дата начала записи")
    time = models.TimeField(verbose_name="Время начала записи")
    commentary = models.TextField(verbose_name="Комментарий",null=True,blank=True)

    class Meta:
        managed = True
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return str(self.date)

