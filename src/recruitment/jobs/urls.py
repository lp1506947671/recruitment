from django.urls import path

from . import views

urlpatterns = [
    # 职位列表
    path("", views.joblist, name="joblist"),
    path("job/<int:job_id>/", views.detail, name="detail"),
]
