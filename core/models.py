from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import uuid

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    class Meta:
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.name)

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    image = models.URLField(verbose_name="Изображение", null=True, blank=True)
    views = models.IntegerField(verbose_name="Просмотры", default=0)
    likes = models.IntegerField(verbose_name="Лайки", default=0)
    category = models.ForeignKey(Category,verbose_name="Категория", on_delete=models.CASCADE)
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

class ReviewUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Мастер")
    title = models.CharField(max_length=100,verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст")

    class Meta:
        managed = True
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return str(self.title)