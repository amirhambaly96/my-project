from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import RIG,Lecturer,Publication,ResearchGrant,Performance

@admin.register(RIG)
class ViewAdmin(ImportExportModelAdmin):
	pass
@admin.register(Lecturer)
class ViewAdmin(ImportExportModelAdmin):
	pass
@admin.register(Publication)
class ViewAdmin(ImportExportModelAdmin):
	pass
@admin.register(ResearchGrant)
class ViewAdmin(ImportExportModelAdmin):
	pass
@admin.register(Performance)
class ViewAdmin(ImportExportModelAdmin):
	pass