# Generated by Django 2.0.5 on 2019-10-27 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否删除', verbose_name='是否删除')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
            ],
            options={
                'verbose_name': '用户登录信息表',
                'db_table': 'account_login',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='用户id')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否删除', verbose_name='是否删除')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户注册表',
                'db_table': 'account_user',
            },
        ),
    ]
