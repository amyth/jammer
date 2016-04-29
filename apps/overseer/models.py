from django.db import models


class String(models.Model):
    content = models.CharField(max_length=244)
    is_normalized = models.BooleanField(default=False)
    normalized_id = models.IntegerField(null=True, blank=True)


class Institute(String):
    pass


class Company(String):
    class Meta:
        verbose_name_plural = 'Companies'


class Skill(String):
    pass
