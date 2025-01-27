from django.db import models


# Admin-managed models
class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class SkillType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    skill_type = models.ForeignKey(
        SkillType, on_delete=models.CASCADE, related_name="skills"
    )
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.skill_type.name} - {self.name}"


class Language(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
