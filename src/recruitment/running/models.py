from django.db import models


class Countries(models.Model):
    continent_id = models.IntegerField(blank=True, null=True)
    code = models.TextField()
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    cname = models.TextField(blank=True, null=True)
    full_cname = models.TextField(blank=True, null=True)
    lower_name = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "countries"

    def __str__(self):
        return self.cname if self.cname else self.full_cname if self.full_cname else ""


class States(models.Model):
    country_id = models.ForeignKey(
        Countries, db_column="country_id", null=True, on_delete=models.SET_NULL
    )
    code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cname = models.TextField(blank=True, null=True)
    lower_name = models.TextField(blank=True, null=True)
    code_full = models.TextField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "states"

    def __str__(self):
        return self.cname if self.cname else self.name if self.name else ""


class Cities(models.Model):
    state_id = models.ForeignKey(
        States, db_column="state_id", null=True, on_delete=models.SET_NULL
    )
    code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cname = models.TextField(blank=True, null=True)
    lower_name = models.TextField(blank=True, null=True)
    code_full = models.TextField()

    class Meta:
        managed = False
        db_table = "cities"

    def __str__(self):
        return self.cname if self.cname else self.name if self.name else ""


class Regions(models.Model):
    city_id = models.ForeignKey(
        Cities, db_column="city_id", null=True, on_delete=models.SET_NULL
    )
    code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cname = models.TextField(blank=True, null=True)
    lower_name = models.TextField(blank=True, null=True)
    code_full = models.TextField()

    class Meta:
        managed = False
        db_table = "regions"

    def __str__(self):
        return self.cname if self.cname else self.name if self.name else ""
