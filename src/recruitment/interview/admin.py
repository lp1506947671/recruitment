import codecs
import csv
import logging
from datetime import datetime

from django.contrib import admin, messages
from django.db.models import Q
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from interview import candidate_field as cf
from interview import dingtalk
from interview.models import Candidate
from jobs.models import Resume

logger = logging.getLogger("operate_logger")

exportable_fields = (
    "username",
    "city",
    "phone",
    "bachelor_school",
    "master_school",
    "degree",
    "first_result",
    "first_interviewer_user",
    "second_result",
    "second_interviewer_user",
    "hr_result",
    "hr_score",
    "hr_remark",
    "hr_interviewer_user",
)


def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = "attachment; filename=%s-list-%s.csv" % (
        "recruitment-candidates",
        datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
    )
    response.write(codecs.BOM_UTF8)

    field_list = exportable_fields
    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )
    for obj in queryset:
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            # 修复3：确保字符串字段使用UTF-8编码
            if isinstance(field_value, str):
                csv_line_values.append(field_value)
            else:
                csv_line_values.append(str(field_value))
        writer.writerow(csv_line_values)
    logger.info(
        " %s has exported %s candidate records" % (request.user.username, len(queryset))
    )
    return response


export_model_as_csv.short_description = "导出为CSV文件"
export_model_as_csv.allowed_permissions = ("export",)


# 通知一面面试官面试
def notify_interviewer(modeladmin, request, queryset):
    candidates = ""
    interviewers = ""
    for obj in queryset:
        candidates = obj.username + ";" + candidates
        interviewers = obj.first_interviewer_user.username + ";" + interviewers
    # 这里的消息发送到钉钉， 或者通过 Celery 异步发送到钉钉
    # send ("候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s" % (candidates, interviewers) )
    dingtalk.send(
        "候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s"
        % (candidates, interviewers)
    )
    messages.add_message(request, messages.INFO, "已经成功发送面试通知")


notify_interviewer.short_description = "通知一面面试官"


# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    def get_resume(self, obj):
        if not obj.phone:
            return ""
        resumes = Resume.objects.filter(phone=obj.phone)
        if resumes and len(resumes) > 0:
            return mark_safe(
                '<a href="/resume/%s" target="_blank">%s</a'
                % (resumes[0].id, "查看简历")
            )
        return ""

    get_resume.short_description = "查看简历"
    get_resume.allow_tags = True

    # 当前用户是否有导出权限：
    def has_export_permission(self, request):
        opts = self.opts
        return request.user.has_perm("%s.%s" % (opts.app_label, "export"))

    @staticmethod
    def get_group_names(user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names

    def get_readonly_fields(self, request, obj=None):
        group_names = self.get_group_names(request.user)

        if "interviewer" in group_names:
            return (
                "first_interviewer_user",
                "second_interviewer_user",
            )
        return ()

    def get_list_editable(self, request):
        group_names = self.get_group_names(request.user)

        if request.user.is_superuser or "hr" in group_names:
            return (
                "first_interviewer_user",
                "second_interviewer_user",
            )
        return ()

    def get_changelist_instance(self, request):
        self.list_editable = self.get_list_editable(request)
        return super(CandidateAdmin, self).get_changelist_instance(request)

    # 一面面试官仅填写一面反馈， 二面面试官可以填写二面反馈
    def get_fieldsets(self, request, obj=None):
        group_names = self.get_group_names(request.user)

        if "interview" in group_names and obj.first_interviewer_user == request.user:
            return cf.default_fieldsets_first
        if "interview" in group_names and obj.second_interviewer_user == request.user:
            return cf.default_fieldsets_second
        return cf.default_fieldsets

    # 对于非管理员，非HR，获取自己是一面面试官或者二面面试官的候选人集合:s
    def get_queryset(self, request):  # show data only owned by the user
        qs = super(CandidateAdmin, self).get_queryset(request)

        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or "hr" in group_names:
            return qs
        return Candidate.objects.filter(
            Q(first_interviewer_user=request.user)
            | Q(second_interviewer_user=request.user)
        )

    actions = (export_model_as_csv, notify_interviewer)
    # 右侧筛选条件
    list_filter = (
        "city",
        "first_result",
        "second_result",
        "hr_result",
        "first_interviewer_user",
        "second_interviewer_user",
        "hr_interviewer_user",
    )

    # 查询字段
    search_fields = ("username", "phone", "email", "bachelor_school")

    # 列表页排序字段
    ordering = (
        "hr_result",
        "second_result",
        "first_result",
    )

    exclude = ("creator", "created_date", "modified_date")
    list_display = (
        "username",
        "city",
        "bachelor_school",
        "get_resume",
        "first_score",
        "first_result",
        "first_interviewer_user",
        "second_score",
        "second_result",
        "second_interviewer_user",
        "hr_score",
        "hr_result",
        "hr_interviewer_user",
    )
    fieldsets = (
        (
            "基础信息",
            {
                "fields": (
                    "username",
                    "city",
                    "phone",
                    "email",
                    "apply_position",
                    "gender",
                    "candidate_remark",
                    "bachelor_school",
                    "master_school",
                    "doctor_school",
                    "major",
                    "degree",
                    "test_score_of_general_ability",
                    "last_editor",
                )
            },
        ),
        (
            "一面信息",
            {
                "fields": (
                    "first_score",
                    "first_learning_ability",
                    "first_professional_competency",
                    "first_advantage",
                    "first_result",
                    "first_recommend_position",
                    "first_interviewer_user",
                    "first_remark",
                )
            },
        ),
        (
            "二面信息",
            {
                "fields": (
                    "second_score",
                    "second_learning_ability",
                    "second_professional_competency",
                    "second_pursue_of_excellence",
                    "second_communication_ability",
                    "second_pressure_score",
                    "second_advantage",
                    "second_disadvantage",
                    "second_result",
                    "second_recommend_position",
                    "second_interviewer_user",
                    "second_remark",
                )
            },
        ),
        (
            "HR面试信息",
            {
                "fields": (
                    "hr_score",
                    "hr_responsibility",
                    "hr_communication_ability",
                    "hr_logic_ability",
                    "hr_potential",
                    "hr_stability",
                    "hr_advantage",
                    "hr_disadvantage",
                    "hr_result",
                    "hr_interviewer_user",
                    "hr_remark",
                )
            },
        ),
    )


admin.site.register(Candidate, CandidateAdmin)
