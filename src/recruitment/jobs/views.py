# Create your views here
from django.http import HttpResponse
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
