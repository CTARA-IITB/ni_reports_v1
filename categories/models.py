from django.db import models

class UtAreaEn(models.Model):
    area_nid = models.IntegerField()
    area_parent_nid = models.IntegerField()
    area_id = models.CharField(max_length=30)
    area_name = models.CharField(max_length=100)
    area_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ut_area_en'