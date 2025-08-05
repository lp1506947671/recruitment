from django.contrib import admin
from interview.models import Candidate


# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
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


admin.site.register(Candidate, CandidateAdmin)
