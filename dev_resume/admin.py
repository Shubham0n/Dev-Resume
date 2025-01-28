from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from dev_resume.models import (
    DeveloperProfile,
    DeveloperEducation,
    DeveloperExperience,
    DeveloperProject,
    DeveloperLanguage,
)


# Inline models
class DeveloperEducationInline(admin.TabularInline):
    model = DeveloperEducation
    extra = 0


class DeveloperExperienceInline(admin.StackedInline):
    model = DeveloperExperience
    autocomplete_fields = ["role"]
    extra = 0


class DeveloperProjectInline(admin.StackedInline):
    model = DeveloperProject
    autocomplete_fields = ["key_skills", "developer_role"]
    extra = 0


class DeveloperLanguageInline(admin.TabularInline):
    model = DeveloperLanguage
    autocomplete_fields = ["language_name"]
    extra = 0


# Developer Profile Admin
@admin.register(DeveloperProfile)
class DeveloperProfileAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "email",
        "phone_number",
        "total_experience",
        "role",
    )
    search_fields = ("name", "email", "phone_number")
    list_filter = ("total_experience", "role")
    readonly_fields = ("slug",)
    autocomplete_fields = ["skills", "role"]
    inlines = [
        DeveloperEducationInline,
        DeveloperExperienceInline,
        DeveloperProjectInline,
        DeveloperLanguageInline,
    ]
