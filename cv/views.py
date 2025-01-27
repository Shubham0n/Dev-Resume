from django.shortcuts import render, get_object_or_404
from .models import DeveloperProfile


def resume_view(request):
    if request.GET.get("name", None):
        resume = get_object_or_404(
            DeveloperProfile,
            name=request.GET.get("name"),
        )
    else:
        resume = DeveloperProfile.objects.first()

    if not resume:
        return render(request, "example.html", {"error": "No resume found"})

    context = {
        "name": resume.name,
        "phone": resume.phone_number,
        "email": resume.email,
        "objective": resume.objective,
        "skills": resume.get_skills(),
        "experiences": resume.experience.all(),
        "projects": resume.projects.all(),
        "educations": resume.education.all(),
        "languages": resume.languages.all(),
        "developer_list": DeveloperProfile.objects.values_list(
            "name",
            flat=True,
        ),
    }

    return render(request, "cv.html", context)
