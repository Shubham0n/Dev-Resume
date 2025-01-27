from django.db import models
from itertools import groupby
from tinymce.models import HTMLField
from admin_portal.models import Skill, Role, Language, Degree


# Developer models
class DeveloperProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    objective = models.TextField()
    address = models.TextField()
    total_experience = models.FloatField(help_text="Total experience in years")
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    skills = models.ManyToManyField(Skill, related_name="developers_skills")

    def __str__(self):
        return self.name

    def get_skills(self):
        skills = self.skills.values("name", "skill_type__name").order_by(
            "skill_type__name"
        )

        grouped_skills = {
            skill_type: list(items)
            for skill_type, items in groupby(
                skills, key=lambda x: x["skill_type__name"]
            )
        }
        return grouped_skills


class DeveloperEducation(models.Model):
    developer = models.ForeignKey(
        DeveloperProfile, on_delete=models.CASCADE, related_name="education"
    )
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)
    university = models.CharField(max_length=255)
    cgpa = models.FloatField(null=True, blank=True)
    sgpa = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} at {self.university}"


class DeveloperExperience(models.Model):
    developer = models.ForeignKey(
        DeveloperProfile, on_delete=models.CASCADE, related_name="experience"
    )
    company_name = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    job_description = HTMLField(
        default="""
        <ul>
            <li>JD 1</li>
            <li>JD 2</li>
            <li>JD 3</li>
        </ul>
        """
    )

    def __str__(self):
        return f"{self.role} at {self.company_name}"


class DeveloperProject(models.Model):
    developer = models.ForeignKey(
        DeveloperProfile, on_delete=models.CASCADE, related_name="projects"
    )
    title = models.CharField(max_length=255)
    developer_role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
    )
    key_skills = models.ManyToManyField(Skill, related_name="projects")
    description = HTMLField(
        default="""
        <ul>
            <li>Description 1</li>
            <li>Description 2</li>
            <li>Description 3</li>
        </ul>
        """
    )

    def __str__(self):
        return self.title


class DeveloperLanguage(models.Model):
    class LevelChoices(models.TextChoices):
        NATIVE_BILINGUAL = (
            "Native or Bilingual Proficiency",
            "Native or Bilingual",
        )
        FULL_PROFESSIONAL = (
            "Full Professional Proficiency",
            "Full Professional",
        )
        PROFESSIONAL_WORKING = (
            "Professional Working Proficiency",
            "Professional Working",
        )
        LIMITED_WORKING = (
            "Limited Working Proficiency",
            "Limited Working",
        )
        ELEMENTARY = (
            "Elementary Proficiency",
            "Elementary",
        )
        BEGINNER = (
            "Beginner",
            "Beginner",
        )

    developer = models.ForeignKey(
        DeveloperProfile, on_delete=models.CASCADE, related_name="languages"
    )
    language_name = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
    )
    level = models.CharField(max_length=255, choices=LevelChoices.choices)

    def __str__(self):
        return self.language_name.name
