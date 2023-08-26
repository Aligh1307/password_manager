from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Password(models.Model):
    name = models.CharField(max_length=250, verbose_name='نام')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', verbose_name='کاربر')
    password = models.CharField(max_length=250, verbose_name='رمز عبور')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)

    def __str__(self):
        return self.name

