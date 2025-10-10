from django.db import models


class Area(models.Model):
    country_id = models.IntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cname = models.TextField(blank=True, null=True)
    lower_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "area"


class Cities(models.Model):
    state_id = models.IntegerField()
    code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cname = models.TextField(blank=True, null=True)
    lower_name = models.TextField(blank=True, null=True)
    code_full = models.TextField()

    class Meta:
        managed = False
        db_table = "cities"


class Continents(models.Model):
    name = models.TextField(blank=True, null=True)
    cname = models.TextField(blank=True, null=True)
    lower_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "continents"


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


class Regions(models.Model):
    city_id = models.IntegerField()
    code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cname = models.TextField(blank=True, null=True)
    lower_name = models.TextField(blank=True, null=True)
    code_full = models.TextField()

    class Meta:
        managed = False
        db_table = "regions"


class States(models.Model):
    country_id = models.IntegerField()
    code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cname = models.TextField(blank=True, null=True)
    lower_name = models.TextField(blank=True, null=True)
    code_full = models.TextField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "states"
