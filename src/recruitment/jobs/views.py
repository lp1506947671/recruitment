# Create your views here
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.generic import CreateView, DetailView

from .forms import ResumeForm
from .models import JOB_TYPES, Cities, Job, Resume


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


class ResumeCreateView(LoginRequiredMixin, CreateView):
    """简历职位页面"""

    template_name = "resume_form.html"
    success_url = "/joblist/"
    model = Resume
    fields = [
        "username",
        "city",
        "phone",
        "email",
        "apply_position",
        "gender",
        "bachelor_school",
        "master_school",
        "major",
        "degree",
        "picture",
        "attachment",
        "candidate_introduction",
        "work_experience",
        "project_experience",
    ]

    def post(self, request, *args, **kwargs):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {"form": form})

    # 从 URL 请求参数带入默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ResumeDetailView(DetailView):
    """简历详情页"""

    model = Resume
    template_name = "resume_detail.html"
