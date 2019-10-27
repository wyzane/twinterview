from django.db import models

from core.models import (DateTimeModel,
                         DeletedModel)


class JobInfo(DateTimeModel,
              DeletedModel,
              models.Model):

    DISPLAY_FIELDS = ("job_id", "name", "status", "modified")

    job_status = (
        (0, "waiting"),
        (1, "running"),
        (2, "finish")
    )

    user_id = models.IntegerField(
        verbose_name="用户id")
    job_id = models.CharField(
        max_length=256,
        verbose_name="任务id")
    name = models.CharField(
        max_length=64,
        verbose_name="job名称")
    status = models.IntegerField(
        choices=job_status,
        default=0,
        verbose_name="job状态")
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name="更新时间")

    class Meta:
        db_table = "job_info"
        verbose_name = "job信息表"
