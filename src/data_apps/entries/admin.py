from django.contrib import admin
from entries.models import Sprint, Project, DeelTaak, TijdEntry

# Register your models here.
class SprintAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class DeelTaakAdmin(admin.ModelAdmin):
    pass

class TijdEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sprint, SprintAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(DeelTaak, DeelTaakAdmin)
admin.site.register(TijdEntry, TijdEntryAdmin)
