from django.contrib import admin
from .models import (
        Institute,
        Company,
        Skill
)


admin.site.register(Institute)
admin.site.register(Company)
admin.site.register(Skill)
