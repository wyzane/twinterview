from django.db import models

from core.models import (DateTimeModel,
                         DeletedModel)


class User(DateTimeModel,
           DeletedModel,
           models.Model):

    user_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name="用户id")
    username = models.CharField(
        max_length=32,
        verbose_name="用户名")
    password = models.CharField(
        max_length=256,
        verbose_name="密码")

    class Meta:
        db_table = "account_user"
        verbose_name = "用户注册表"


class Login(DateTimeModel,
            DeletedModel,
            models.Model):

    user_id = models.IntegerField(
        verbose_name="用户id")

    class Meta:
        db_table = "account_login"
        verbose_name = "用户登录信息表"
