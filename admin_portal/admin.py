from django.contrib import admin
from .models import Role, SkillType, Skill, Language, Degree
from import_export.admin import ImportExportModelAdmin
from import_export import resources


# ==========================
# Import-Export Resources
# ==========================


class RoleResource(resources.ModelResource):
    class Meta:
        model = Role


class SkillTypeResource(resources.ModelResource):
    class Meta:
        model = SkillType


class SkillResource(resources.ModelResource):
    class Meta:
        model = Skill


class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language


class DegreeResource(resources.ModelResource):
    class Meta:
        model = Degree


# ==========================
# Admin Panels
# ==========================


# Admin-only models with Import/Export
@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin):
    resource_class = RoleResource
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(SkillType)
class SkillTypeAdmin(ImportExportModelAdmin):
    resource_class = SkillTypeResource
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Skill)
class SkillAdmin(ImportExportModelAdmin):
    resource_class = SkillResource
    list_display = ("name", "skill_type")
    search_fields = ("name",)
    list_filter = ("skill_type",)


@admin.register(Language)
class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Degree)
class DegreeAdmin(ImportExportModelAdmin):
    resource_class = DegreeResource
    list_display = ("name",)
    search_fields = ("name",)
