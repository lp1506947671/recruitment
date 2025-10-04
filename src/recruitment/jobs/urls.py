from django.urls import path

from . import views

urlpatterns = [
    # 职位列表
    path("joblist/", views.joblist, name="joblist"),
    path("job/<int:job_id>/", views.detail, name="detail"),
    path("resume/add/", views.ResumeCreateView.as_view(), name="resume-add"),
    path("", views.joblist),
]
