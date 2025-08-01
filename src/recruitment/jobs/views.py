# Create your views here
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import JOB_TYPES, Cities, Job


def joblist(request):
    job_list = Job.objects.order_by("job_type")
    template = loader.get_template("jobs/joblist.html")
    context = {"job_list": job_list}
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JOB_TYPES[job.job_type][1]
    return HttpResponse(template.render(context, request))


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, "jobs/job.html", {"job": job})
