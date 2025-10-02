import codecs
import csv
from datetime import datetime

from django.contrib import admin
from django.http import HttpResponse
from interview.models import Candidate

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

    return response


export_model_as_csv.short_description = "导出为CSV文件"


# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    actions = (export_model_as_csv,)
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
