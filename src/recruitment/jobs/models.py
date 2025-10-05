# Create your models here.
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from registration.models import RegistrationProfile

RegistrationProfile._meta.verbose_name = "注册"
RegistrationProfile._meta.verbose_name_plural = "注册"

JOB_TYPES = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "设计类"),
    (4, "市场营销类"),
]
Cities = [(0, "北京"), (1, "上海"), (2, "深圳"), (3, "杭州"), (4, "广州")]
DEGREE_TYPE = (("本科", "本科"), ("硕士", "硕士"), ("博士", "博士"))


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


DEGREE_TYPE = (("本科", "本科"), ("硕士", "硕士"), ("博士", "博士"))


class Resume(models.Model):
    # Translators: 简历实体的翻译
    username = models.CharField(max_length=135, verbose_name=_("姓名"))
    applicant = models.ForeignKey(
        User, verbose_name=_("申请人"), null=True, on_delete=models.SET_NULL
    )
    city = models.CharField(max_length=135, verbose_name=_("城市"))
    phone = models.CharField(max_length=135, verbose_name=_("手机号码"))
    email = models.EmailField(max_length=135, blank=True, verbose_name=_("邮箱"))
    apply_position = models.CharField(
        max_length=135, blank=True, verbose_name=_("应聘职位")
    )
    born_address = models.CharField(
        max_length=135, blank=True, verbose_name=_("生源地")
    )
    gender = models.CharField(max_length=135, blank=True, verbose_name=_("性别"))
    picture = models.ImageField(
        upload_to="images/", blank=True, verbose_name=_("个人照片")
    )
    attachment = models.FileField(
        upload_to="file/", blank=True, verbose_name=_("简历附件")
    )

    # 学校与学历信息
    bachelor_school = models.CharField(
        max_length=135, blank=True, verbose_name=_("本科学校")
    )
    master_school = models.CharField(
        max_length=135, blank=True, verbose_name=_("研究生学校")
    )
    doctor_school = models.CharField(
        max_length=135, blank=True, verbose_name="博士生学校"
    )
    major = models.CharField(max_length=135, blank=True, verbose_name=_("专业"))
    degree = models.CharField(
        max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=_("学历")
    )
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)

    # 候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(
        max_length=1024, blank=True, verbose_name="自我介绍"
    )
    work_experience = models.TextField(
        max_length=1024, blank=True, verbose_name="工作经历"
    )
    project_experience = models.TextField(
        max_length=1024, blank=True, verbose_name="项目经历"
    )

    class Meta:
        verbose_name = _("简历")
        verbose_name_plural = _("简历列表")

    def __str__(self):
        return self.username
