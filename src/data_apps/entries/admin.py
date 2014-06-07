from django.contrib import admin
from entries.models import Sprint, Project

# Register your models here.
class SprintAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sprint, SprintAdmin)
admin.site.register(Project, ProjectAdmin)
