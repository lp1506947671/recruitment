from django.apps import AppConfig, apps
from django.contrib import admin


class AdminClass(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        # 列表页自动显示所有的字段：
        self.list_display = [field.name for field in model._meta.fields]
        super(AdminClass, self).__init__(model, admin_site)


# automatically register all models
class RunningConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "running"

    def ready(self):
        models = apps.get_app_config("running").get_models()
        for model in models:
            try:
                admin.site.register(model, AdminClass)
            except admin.sites.AlreadyRegistered:
                pass
