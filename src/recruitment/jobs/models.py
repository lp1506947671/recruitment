# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

JOB_TYPES = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "设计类"),
    (4, "市场营销类"),
]
Cities = [(0, "北京"), (1, "上海"), (2, "深圳"), (3, "杭州"), (4, "广州")]


class Job(models.Model):
    job_name = models.CharField(max_length=250, blank=False, verbose_name=_("职位名称"))
    job_type = models.SmallIntegerField(
        blank=False, choices=JOB_TYPES, verbose_name=_("职位类型")
    )
    job_city = models.SmallIntegerField(
        blank=False, choices=Cities, verbose_name=_("工作城市")
    )
    job_responsibility = models.TextField(
        max_length=1024, blank=False, verbose_name=_("工作职责")
    )
    job_requirement = models.TextField(
        max_length=1024, blank=False, verbose_name=_("工作职责")
    )
    creator = models.ForeignKey(
        User, verbose_name=_("创建人"), on_delete=models.SET_NULL, null=True
    )
    # auto_now_add 仅在对象首次创建时赋值,auto_now 每次保存对象时都会赋值。
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("创建日期"))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_("修改日期"))

    class Meta:
        db_table = "tb_job"
        verbose_name = _("职位")
        verbose_name_plural = _("职位")
