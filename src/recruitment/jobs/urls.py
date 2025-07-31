from django.urls import path

from . import views

urlpatterns = [
    # 职位列表
    path("joblist/", views.joblist, name="joblist"),
]
