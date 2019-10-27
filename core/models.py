from django.db import models


class DateTimeModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间",
        help_text="创建时间")

    class Meta:
        abstract = True


class DeletedModel(models.Model):
    is_deleted = models.BooleanField(
        default=False,
        verbose_name="是否删除",
        help_text="是否删除")

    class Meta:
        abstract = True
